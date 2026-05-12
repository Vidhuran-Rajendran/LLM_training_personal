import chromadb.config
from collections import OrderedDict,deque
from rank_bm25 import BM25Okapi
from nltk.corpus import stopwords
import math
from math import sqrt
import ollama
import re
import shutil,os
if os.path.exists("./vectorstore"):
    shutil.rmtree("./vectorstore")
class VectorStore:
    def __init__(self,path = ".\vectorstore",collection_name ="dsa_docs"):
        self.client = chromadb.PersistentClient(path=path)
        self.collection = self.client.get_or_create_collection(name=collection_name)
    
    def add_chunks(self,chunks,embed_fn):
        existing = self.collection.count()
        if existing>0:
            print("Loading_existing")
        existing_ids = set(self.collection.get()["ids"])
        new_chunks,new_embeddings,new_ids = [],[],[]

        print("Building new vector store")
        for idx,chunk in enumerate(chunks):
            id_ = str(idx)
            if id_ not in existing_ids:
                new_chunks.append(chunk)
                new_embeddings.append(embed_fn(chunk))
                new_ids.append(id_)
        
        if new_chunks:
            self.collection.add(documents=new_chunks,embeddings=new_embeddings,ids=new_ids)
            print(f"Added{len(new_chunks)} new chunks")
        
    def search(self,query_vector,top_k=3):
        result = self.collection.query(query_embeddings=[query_vector],n_results=top_k)
        return result["documents"][0] if result["documents"] else []

def reciprocal_rank_fusion(bm25_chunks, chroma_chunks, k=60):
    scores = {}

    for rank, chunk in enumerate(bm25_chunks):
        scores[chunk] = scores.get(chunk, 0) + 1 / (rank + k)

    for rank, chunk in enumerate(chroma_chunks):
        scores[chunk] = scores.get(chunk, 0) + 1 / (rank + k)

    # sort by highest score
    return sorted(scores.items(), key=lambda x: x[1], reverse=True)


class BM25Search:
    def __init__(self):
        self.bm25 = None
        self.chunks = []
    def build(self,chunks):
        self.chunks = chunks
        tokenized = [re.findall(r'\b\w+\b', chunk.lower()) for chunk in chunks]
        self.bm25 = BM25Okapi(tokenized)
    def search(self, query, top_k=3):
        if self.bm25 is None:
            return []

        query_tokens = query.lower().split()
        scores = self.bm25.get_scores(query_tokens)

        top_indices = sorted(range(len(scores)),key=lambda i: scores[i],reverse=True)

        # ✅ FILTER chunks containing query words
        filtered = []
        for i in top_indices:
            chunk = self.chunks[i].lower()
            if all(q in chunk for q in query_tokens):
                filtered.append(self.chunks[i])
            if len(filtered) == top_k:
                break
        #print("BM25 filtered:", filtered)
        return filtered if filtered else [self.chunks[i] for i in top_indices[:top_k]]

class DocumentLoader():
    def __init__(self,vector_store):
        self.chunks = []
        self.embedded_chunks = []
        self.text = ""
        self.vector_store = vector_store
        self.bm25 = BM25Search()
        
    # Change this line in your loader class:
    def load_file(self, path):
        with open(path, encoding="utf-8") as f:  # <--- Add encoding here
            self.text = f.read()
        return self.text
    
    def chunks_creation(self, size=500, overlap=100):
        # Split on any markdown heading (# or ##)
        sections = re.split(r'\n#{1,2} ', self.text)
        self.chunks = []
        for sec in sections:
            sec = sec.strip()
            if len(sec) > 30:  # lower threshold — 50 was too strict
                self.chunks.append(sec)
        return self.chunks
    
    def embed_all_chunks(self,embed_fn):
        self.vector_store.add_chunks(self.chunks,embed_fn)
        self.bm25.build(self.chunks)
        
    
    def top_3_chunks(self,qurey_vector):
        return self.vector_store.search(qurey_vector,top_k=3)


class ChatMemory:

    def __init__(self,model = "qwen2.5",system_prompt = "be a tutor",max_tokens=3000,cache_size=10,path=None):
        self.model = model
        self.max_tokens = max_tokens
        self.cache_size = cache_size
        self.chat_history = deque([{"role":"system","content":system_prompt}])
        self.cache = OrderedDict()
        self.ai_counter = 0
        self.cache_counter = 0
        self.stack = []
        self.observation_cache = {}
        
        self.vector_store = VectorStore(
            path="./vectorstore",
            collection_name="dsa_docs"
        )

        self.loader = DocumentLoader(self.vector_store)
        self.path = path
        self.doc_text = ''
        
   
    # ---------------- NORMALIZE ----------------
    def normalize(self, text):
        return re.sub(r'[^\w\s]', '', text).strip().lower()

    # ---------------- EMBEDDING ----------------
    def embed(self, text):
        return ollama.embeddings(
            model=self.model,
            prompt=text
        )["embedding"]

    # ---------------- DOCUMENT ----------------
    def prepare_document(self, path, size=1000, overlap=10):
        self.loader.load_file(path)
        self.loader.chunks_creation(size, overlap)
        print("Total chunks created:", len(self.loader.chunks))

        for i, c in enumerate(self.loader.chunks[:5]):
            print(f"Chunk {i} preview:", c[:200])
        self.loader.embed_all_chunks(self.embed)

    # ---------------- RETRIEVAL ----------------    
    #retriving the context where it is availabe in the doc or not
    def retrive_context(self,user_text):
        history_text = " ".join([m["content"]for  m in list(self.chat_history)[-3:]])
        
        full_query = history_text + " " + user_text
        embedded_user = self.embed(full_query)
        chroma_chunks  = self.loader.top_3_chunks(embedded_user)
        bm25_chunks = self.loader.bm25.search(full_query, top_k=3)

        #print("BM25 Chunks:", bm25_chunks)
        #print("Chroma Chunks:", chroma_chunks)
        
        merged = reciprocal_rank_fusion(bm25_chunks, chroma_chunks)
        top_chunks = [chunk for chunk, score in merged[:3]]
        if not top_chunks:
            return "No Context Found"
        
        #combined = " ".join (top_chunks)
        # if len(combined.split())<15:
        #     return "No Context Found"
        #print("DEBUG:", top_chunks)
        return "\n\n".join(top_chunks)
    
    # ---------------- TOKEN ----------------
    def count_tokens(self, text):
        return len(text) // 4

    def total_tokens(self):
        content = " ".join(m["content"] for m in self.chat_history)
        return self.count_tokens(content)
    
    def trim_to_budget(self):
        while self.total_tokens()>self.max_tokens:
            del self.chat_history[1]
            del self.chat_history[1]
    
    def trim_history(self):
        while len(self.chat_history)>10:
            self.chat_history.popleft()
            
    # ---------------- HISTORY ----------------     
    #adding user input & reply to the history 
    def add_user(self, text):
        text = self.normalize(text)
        self.chat_history.append({"role":"user","content":text})
        self.trim_to_budget()
        return text
    
    def add_assistant(self,text):
        self.chat_history.append({"role":"assistant","content":text})
        
    def get_history(self):
        return list(self.chat_history)
    
    # ---------------- CACHE ----------------
    def check_cache(self,text):
        if text in self.cache:
            self.cache_counter+=1
            return self.cache[text]
        else: return None
    
    def store_cache(self,text,ai_reply):
        if len(self.cache)>=self.cache_size:
            self.cache.popitem(last=False)
        self.cache[text] = ai_reply
        self.ai_counter+=1
        
    def get_stats(self):
        total = self.cache_counter + self.ai_counter
        if total == 0:
            return "hit rate: 0%"
        return f"hit rate: {(self.cache_counter / total) * 100:.2f}%"
    
    # ---------------- TOOLS ----------------
    def execute_action(self, action):

        if action.startswith("search"):
            query = action[len('search("'):-2]
            return self.retrive_context(query)

        elif action.startswith("calculate"):
            expr = action[len('calculate("'):-2]
            try:
                return str(eval(expr))
            except:
                return "calculation error"

        elif action.startswith("history"):
            history = list(self.chat_history)[1:]
            return "\n".join(f"{h['role']}: {h['content']}" for h in history)

        return "Unknown action"
    
    
    def react_chat(self,user_input):
    
        context = """
You are a ReAct agent.

You MUST follow this format:

Thought: reasoning step
Action: tool_name("input")
Observation: result
Final Answer: answer

INSTRUCTIONS:

- Always try to use the search tool FIRST for any data structure or algorithm question.
- Use the information returned by the tool as your primary source.
- If the retrieved context is relevant, use it to answer clearly.
- If the context is PARTIAL, still answer using the best available information.
- Only say "Context not available in the provided document." 
  if no useful context is found at all.

RULES:

- Prefer using the search tool.
- Do NOT skip calling a tool.
- Do NOT invent observations.
- Use ONE action at a time.
- Keep answers concise and based on context.

"""

        history = "\n".join([f"{m['role']}: {m['content']}" for m in list(self.chat_history)])
        context += f"\nConversation History:\n{history}\n"
        context += f"\nUser Question: {user_input}\n"

        action_used = False
        MAX_STEPS = 10

        for _ in range(MAX_STEPS):
            response = ollama.chat(
                model=self.model,
                messages=[{"role": "user", "content": context}]
            )["message"]["content"]

            #  Validate structure (force ReAct format)
            # if not ("Thought:" in response and ("Action:" in response or "Final Answer:" in response)):
            #     context += "\nFollow the format strictly. \n"  # add this to guide the model
            #     return "Invalid format: follow ReAct structure"

            # context += response + "\n"
            # print("--------------raw response:", response)

            # ✅ Detect Action
            if "Action:" in response:
                action_used = True
                action_line = [line for line in response.splitlines()if line.startswith("Action:")][0]
                action = action_line.replace("Action:", "").strip()
                if action in self.observation_cache:
                    observation = self.observation_cache[action]
                else:
                    observation = self.execute_action(action)
                    self.observation_cache[action] = observation
                context += f"Observation: {observation}\n"
                continue

            # ✅ Enforce rule on Final Answer
            if "Final Answer:" in response:
                if not action_used:
                    observation = self.execute_action(f'search("{user_input}")')
                    return observation
                return response.split("Final Answer:")[-1].strip()
            
            # ✅ final fallback (IMPORTANT)
            fallback = self.retrive_context(user_input)

            if fallback and fallback != "No Context Found":
                return fallback

        return "Context not available in the provided document."
    
    # ---------------- MAIN ENTRY ----------------
    def chat(self,user_):
        self.trim_history()
        normalized = self.normalize(user_)
        self.chat_history.append({"role":"user","content":user_})
        self.trim_to_budget()
        cached = self.check_cache(normalized)
        if cached:
            reply = cached
        else:
            reply = self.react_chat(user_)
            self.store_cache(normalized,reply)
            
        self.add_assistant(reply)
        return reply 
    
## agent function
#--------------------------------------------------------------------------------------------------------------------------------------------
#TOOL 1: search document
#--------------------------------------------------------------------------------------------------------------------------------------------
def search_document(query,memory):
    return memory.retrive_context(query)

#--------------------------------------------------------------------------------------------------------------------------------------------
#TOOL 2: calculate
#--------------------------------------------------------------------------------------------------------------------------------------------
def calculate(expression):
   try:
       allowed = "0123456789+-*/(). eE"
       cleaned = expression.replace(" ", "")
    #    print(f"DEBUG expression: {repr(cleaned)}")  # add this
       if any(ch not in allowed for ch in cleaned):
           bad = [ch for ch in cleaned if ch not in allowed]
        #    print(f"DEBUG blocked chars: {bad}")  # add this
           return "unsafe expression"
       result = eval(expression, {"__builtins__": None}, vars(math))
    #    print(f"DEBUG result: {result}")  # add this
       return str(result)
   except Exception as e:
       return f"calculation error: {str(e)}"
    
# -------------------------------
# TOOL 3: define_term
# -------------------------------
def define_term(term):
    definitions = {
        "array": "A linear data structure storing elements in contiguous memory.",
        "graph": "A set of nodes connected by edges; can be directed or undirected.",
        "queue": "A FIFO (first-in-first-out) data structure.",
        "stack": "A LIFO (last-in-first-out) data structure.",
        "tree": "A hierarchical data structure with a root and child nodes.",
    }
    term = term.lower().strip()
    return definitions.get(term, "Definition not found.")

# -------------------------------
# TOOL 4: get_history
# -------------------------------
def get_history(memory):
    history = list(memory.chat_history)[1:]
    return "\n".join(f"{m['role']}: {m['content']}" for m in history)

TOOLS = {
    "search": search_document,
    "calculate": calculate,
    "define": define_term,
    "history": get_history
}
memory = ChatMemory()
memory.prepare_document(
    path=r"E:\training\LLM_training\data\final_cleadn_data.md",
    size=200,
    overlap=50)
#print("BM25 result:", memory.loader.bm25.search("binary search"))
# memory.loader.embed_all_chunks(model='qwen2.5')
#print(memory.retrive_context("binary search"))
while True:
    user = input("chat: ")
    print("user :",user)
    if user.lower() == "quit":
        print(memory.get_stats())
        break
    reply = memory.chat(user)
    print("qwen2.5:", reply)
