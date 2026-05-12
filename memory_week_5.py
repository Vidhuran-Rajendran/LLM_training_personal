import chromadb
from collections import OrderedDict, deque
from rank_bm25 import BM25Okapi
import math
import ollama
import re
import shutil
import os

# ==============================================================================
# RECIPROCAL RANK FUSION
# ==============================================================================
def reciprocal_rank_fusion(bm25_chunks, chroma_chunks, k=60):
    scores = {}
    for rank, chunk in enumerate(bm25_chunks):
        scores[chunk] = scores.get(chunk, 0) + 1 / (rank + k)
    for rank, chunk in enumerate(chroma_chunks):
        scores[chunk] = scores.get(chunk, 0) + 1 / (rank + k)
    return sorted(scores.items(), key=lambda x: x[1], reverse=True)

# ==============================================================================
# VECTOR STORE
# ==============================================================================
class VectorStore:
    def __init__(self, path="./vectorstore", collection_name="dsa_docs"):
        self.client = chromadb.PersistentClient(path=path)
        self.collection = self.client.get_or_create_collection(name=collection_name)

    def add_chunks(self, chunks, embed_fn):
        existing = self.collection.count()
        if existing > 0:
            print("Loading existing vector store")

        existing_ids = set(self.collection.get()["ids"])
        new_chunks, new_embeddings, new_ids = [], [], []

        print("Building new vector store")

        for idx, chunk in enumerate(chunks):
            id_ = str(idx)
            if id_ not in existing_ids:
                new_chunks.append(chunk)
                new_embeddings.append(embed_fn(chunk))
                new_ids.append(id_)

        if new_chunks:
            self.collection.add(
                documents=new_chunks,
                embeddings=new_embeddings,
                ids=new_ids
            )
            print(f"Added {len(new_chunks)} new chunks")

    def search(self, query_vector, top_k=3):
        result = self.collection.query(
            query_embeddings=[query_vector], n_results=top_k
        )
        return result["documents"][0] if result["documents"] else []

# ==============================================================================
# BM25 SEARCH
# ==============================================================================
class BM25Search:
    def __init__(self):
        self.bm25 = None
        self.chunks = []

    def build(self, chunks):
        self.chunks = chunks
        tokenized = [re.findall(r'\b\w+\b', chunk.lower()) for chunk in chunks]
        self.bm25 = BM25Okapi(tokenized)

    def search(self, query, top_k=3):
        if self.bm25 is None:
            return []

        query_tokens = re.findall(r'\b\w+\b', query.lower())
        scores = self.bm25.get_scores(query_tokens)

        top_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)

        filtered = []
        for i in top_indices:
            chunk = self.chunks[i].lower()
            if any(q in chunk for q in query_tokens):
                filtered.append(self.chunks[i])
            if len(filtered) == top_k:
                break

        return filtered if filtered else [self.chunks[i] for i in top_indices[:top_k]]

# ==============================================================================
# DOCUMENT LOADER
# ==============================================================================
class DocumentLoader:
    def __init__(self, vector_store):
        self.chunks = []
        self.text = ""
        self.vector_store = vector_store
        self.bm25 = BM25Search()

    def load_file(self, path):
        with open(path, encoding="utf-8") as f:
            self.text = f.read()
        return self.text

    def chunks_creation(self, size=500, overlap=100):
        self.chunks = []

        sections = re.split(r'\n(?=#{1,2} )', self.text)

        for sec in sections:
            sec = sec.strip()
            sec = re.sub(r'\n---+\n?', '\n', sec).strip()

            if len(sec) < 30:
                continue

            words = sec.split()

            if len(words) <= size:
                self.chunks.append(sec)
            else:
                start = 0
                while start < len(words):
                    chunk = " ".join(words[start:start + size])
                    self.chunks.append(chunk)
                    start += (size - overlap)

        return self.chunks

    def embed_all_chunks(self, embed_fn):
        self.vector_store.add_chunks(self.chunks, embed_fn)
        self.bm25.build(self.chunks)

    def top_k_chunks(self, query_vector, top_k=3):
        return self.vector_store.search(query_vector, top_k=top_k)

# ==============================================================================
# CHAT MEMORY + REACT AGENT
# ==============================================================================
class ChatMemory:

    def __init__(self, model="qwen2.5", system_prompt="be a tutor",
                 max_tokens=3000, cache_size=10, path=None):

        self.model = model
        self.max_tokens = max_tokens
        self.cache_size = cache_size
        self.chat_history = deque([{"role": "system", "content": system_prompt}])
        self.cache = OrderedDict()
        self.ai_counter = 0
        self.cache_counter = 0
        self.stack = []

        self.vector_store = VectorStore(path="./vectorstore", collection_name="dsa_docs")
        self.loader = DocumentLoader(self.vector_store)

        self.path = path
        self.doc_text = ""

    def normalize(self, text):
        return re.sub(r'[^\w\s]', '', text).strip().lower()

    def embed(self, text):
        return ollama.embeddings(model=self.model, prompt=text)["embedding"]

    def prepare_document(self, path, size=500, overlap=100):
        self.loader.load_file(path)
        self.loader.chunks_creation(size, overlap)

        print(f"Total chunks created: {len(self.loader.chunks)}")
        for i, c in enumerate(self.loader.chunks):
            print(f"  Chunk {i}: {c[:80]}")

        self.loader.embed_all_chunks(self.embed)

    def retrive_context(self, user_text):
        embedded_user = self.embed(user_text)

        chroma_chunks = self.loader.top_k_chunks(embedded_user, top_k=5)
        bm25_chunks = self.loader.bm25.search(user_text, top_k=5)

        merged = reciprocal_rank_fusion(bm25_chunks, chroma_chunks)

        query_words = user_text.lower().split()

        filtered = []
        for chunk, score in merged:
            text = chunk.lower()
            if any(word in text for word in query_words):
                filtered.append(chunk)
            if len(filtered) == 3:
                break

        if not filtered:
            filtered = [chunk for chunk, _ in merged[:3]]

        return "\n\n".join(filtered)


    def count_tokens(self, text):
        return len(text) // 4

    def total_tokens(self):
        content = " ".join(m["content"] for m in self.chat_history)
        return self.count_tokens(content)

    def trim_to_budget(self):
        while self.total_tokens() > self.max_tokens:
            temp = list(self.chat_history)
            if len(temp) <= 3:
                break
            self.chat_history = deque([temp[0]] + temp[3:])

    def trim_history(self):
        while len(self.chat_history) > 10:
            self.chat_history.popleft()

    def add_assistant(self, text):
        self.chat_history.append({"role": "assistant", "content": text})

    def get_history(self):
        return list(self.chat_history)

    def check_cache(self, text):
        if text in self.cache:
            self.cache_counter += 1
            return self.cache[text]
        return None

    def store_cache(self, text, ai_reply):
        if len(self.cache) >= self.cache_size:
            self.cache.popitem(last=False)
        self.cache[text] = ai_reply
        self.ai_counter += 1

    def get_stats(self):
        total = self.cache_counter + self.ai_counter
        if total == 0:
            return "hit rate: 0%"
        return f"hit rate: {(self.cache_counter / total) * 100:.2f}%"

    def execute_action(self, action):
        match = re.match(r'(\w+)\s*\(\s*["\']?(.*?)["\']?\s*\)\s*$', action.strip(), re.DOTALL)

        if not match:
            return "Unknown action — format: tool_name(\"input\")"

        tool = match.group(1).lower()
        arg = match.group(2).strip()

        if tool == "search":
            return self.retrive_context(arg)

        elif tool == "calculate":
            try:
                allowed_chars = set("0123456789+-*/(). eE")
                cleaned = arg.replace(" ", "")
                bad = [c for c in cleaned if c not in allowed_chars]

                if bad:
                    return f"unsafe expression — blocked: {bad}"

                result = eval(arg, {"__builtins__": None}, vars(math))
                return str(result)

            except Exception as e:
                return f"calculation error: {e}"

        elif tool == "history":
            history = list(self.chat_history)[1:]
            return "\n".join(f"{h['role']}: {h['content']}" for h in history)

        elif tool == "define":
            definitions = {
                "array": "A linear data structure storing elements in contiguous memory.",
                "graph": "A set of nodes connected by edges; can be directed or undirected.",
                "queue": "A FIFO (first-in-first-out) data structure.",
                "stack": "A LIFO (last-in-first-out) data structure.",
                "tree": "A hierarchical data structure with a root and child nodes.",
                "heap": "A complete binary tree where parent <= children (min-heap).",
                "bst": "Binary search tree: left < node <= right, recursive.",
                "avl": "Self-balancing BST — height difference between subtrees <= 1.",
            }
            return definitions.get(arg.lower(), "Definition not found.")

        return f"Unknown tool: {tool}"

    def react_chat(self, user_input):
        observation_cache = {}

        SYSTEM_PROMPT = """You are a ReAct agent. Answer questions using tools only.

Follow this EXACT format every time:
Thought: your reasoning
Action: tool_name("input")
Observation: (system fills this)
Final Answer: your answer

TOOLS:
- search("query")
- calculate("expr")
- history("")
- define("term")

STRICT RULES:
- ALWAYS use an Action before Final Answer
- ONE action per step
- Use only relevant parts of the observation by using tool results
- Ignore unrelated sections

"""

        recent = list(self.chat_history)[-4:]
        history_str = "\n".join(f"{m['role']}: {m['content']}" for m in recent)

        context = SYSTEM_PROMPT
        context += f"\nRecent History:\n{history_str}\n"
        context += f"\nCurrent Question: {user_input}\n"
        context += "\nStart with Thought:\n"

        action_used = False

        for _ in range(8):

            response = ollama.chat(
                model=self.model,
                messages=[{"role": "user", "content": context}]
            )["message"]["content"]

            context += response + "\n"

            if "Action:" in response:
                action_used = True

                action_lines = [line for line in response.splitlines() if line.strip().startswith("Action:")]

                if not action_lines:
                    continue

                action = action_lines[0].replace("Action:", "").strip()

                observation = self.execute_action(action)

                observation_cache[action] = observation

                context += f"Observation: {observation}\n"

                continue

            if "Final Answer:" in response:

                if not action_used:
                    obs = self.execute_action(f'search("{user_input}")')
                    if obs and obs != "No Context Found":
                        return obs
                    return "Context not available in the provided document."

                return response.split("Final Answer:")[-1].strip()

        fallback = self.retrive_context(user_input)

        if fallback and fallback != "No Context Found":
            return fallback

        return "Context not available in the provided document."

    def chat(self, user_):
        self.trim_history()

        normalized = self.normalize(user_)

        self.chat_history.append({"role": "user", "content": user_})

        self.trim_to_budget()

        if re.match(r'^[\d\s\+\-\*\/\(\)\.\^eE]+$', user_.strip()):
            try:
                result = str(eval(user_.strip(), {"__builtins__": None}, vars(math)))
                self.add_assistant(result)
                return result
            except Exception:
                pass

        cached = self.check_cache(normalized)

        if cached:
            self.add_assistant(cached)
            return cached

        reply = self.react_chat(user_)

        self.store_cache(normalized, reply)

        self.add_assistant(reply)

        return reply

# ==============================================================================
# MAIN
# ==============================================================================
if __name__ == "__main__":

    if os.path.exists("./vectorstore"):
        shutil.rmtree("./vectorstore")
        print("Cleared old vectorstore")

    memory = ChatMemory()

    memory.prepare_document(
        path=r"E:\training\LLM_training\data\final_cleadn_data.md",
        size=500,
        overlap=100
    )

    while True:
        user = input("chat: ")
        print("user :", user)

        if user.lower() == "quit":
            print(memory.get_stats())
            break

        reply = memory.chat(user)

        print("qwen2.5:", reply)