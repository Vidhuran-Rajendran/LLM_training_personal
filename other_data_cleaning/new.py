from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
   SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
   PageBreak, HRFlowable, KeepTogether
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.platypus import Flowable
# ── COLORS ──
NAV   = colors.HexColor("#1E3A5F")
BLUE  = colors.HexColor("#2E75B6")
GREEN = colors.HexColor("#2E7D32")
ORG   = colors.HexColor("#E65100")
PUR   = colors.HexColor("#6A1B9A")
LGRAY = colors.HexColor("#F4F6F9")
MGRAY = colors.HexColor("#E0E0E0")
DTEXT = colors.HexColor("#1A1A2E")
MUTED = colors.HexColor("#555555")
CODE  = colors.HexColor("#F0F4FF")
WHITE = colors.white
BLK_COLORS = {
   "DSA Concept": (colors.HexColor("#E3F2FD"), BLUE),
   "DSA Problem": (colors.HexColor("#E8F5E9"), GREEN),
   "AI Concept":  (colors.HexColor("#FFF3E0"), ORG),
   "AI Project":  (colors.HexColor("#F3E5F5"), PUR),
}
EMOJIS = {
   "DSA Concept": "📘",
   "DSA Problem": "🧩",
   "AI Concept":  "🤖",
   "AI Project":  "🔨",
}
W = A4[0] - 28*mm
# ── STYLES ──
def S(name, **kw):
   return ParagraphStyle(name, **kw)
base        = S("base",       fontName="Helvetica",       fontSize=10, leading=15, textColor=DTEXT)
bold_s      = S("bold_s",     fontName="Helvetica-Bold",  fontSize=10, leading=15, textColor=DTEXT)
code_s      = S("code_s",     fontName="Courier",         fontSize=8.5,leading=13, textColor=colors.HexColor("#1A1A2E"), backColor=CODE, leftIndent=6, rightIndent=6)
h_title     = S("h_title",    fontName="Helvetica-Bold",  fontSize=22, leading=28, textColor=WHITE, alignment=TA_CENTER)
h_sub       = S("h_sub",      fontName="Helvetica",       fontSize=11, leading=16, textColor=colors.HexColor("#BDD7EE"), alignment=TA_CENTER)
week_title  = S("week_title", fontName="Helvetica-Bold",  fontSize=16, leading=22, textColor=WHITE)
day_title   = S("day_title",  fontName="Helvetica-Bold",  fontSize=14, leading=20, textColor=WHITE)
block_hdr   = S("block_hdr",  fontName="Helvetica-Bold",  fontSize=11, leading=16, textColor=WHITE)
concept_hdr = S("concept_hdr",fontName="Helvetica-Bold",  fontSize=10, leading=15, textColor=DTEXT)
bullet_s    = S("bullet_s",   fontName="Helvetica",       fontSize=10, leading=15, textColor=DTEXT, leftIndent=12, bulletIndent=0)
think_s     = S("think_s",    fontName="Helvetica-Oblique",fontSize=9.5,leading=14,textColor=colors.HexColor("#4A2800"),leftIndent=8)
think_lbl   = S("think_lbl",  fontName="Helvetica-Bold",  fontSize=9.5,leading=14, textColor=ORG)
verify_s    = S("verify_s",   fontName="Helvetica",       fontSize=10, leading=15, textColor=colors.HexColor("#1B5E20"), leftIndent=12)
reflect_s   = S("reflect_s",  fontName="Helvetica",       fontSize=10, leading=15, textColor=colors.HexColor("#4A148C"), leftIndent=12)
tmrw_s      = S("tmrw_s",     fontName="Helvetica-Oblique",fontSize=9.5,leading=14,textColor=MUTED)
lc_s        = S("lc_s",       fontName="Helvetica",       fontSize=9.5,leading=14, textColor=BLUE)
def sp(h=4): return Spacer(1, h*mm)
def block_header(label):
   bg, fg = BLK_COLORS[label]
   emoji = EMOJIS[label]
   times = {"DSA Concept":"30 min","DSA Problem":"30 min","AI Concept":"20 min","AI Project":"40 min"}
   t = Table([[Paragraph(f"{emoji}  BLOCK — {label}  <font color='#FFFFFF99'>({times[label]})</font>", block_hdr)]],
             colWidths=[W])
   t.setStyle(TableStyle([
       ("BACKGROUND", (0,0), (-1,-1), fg),
       ("ROUNDEDCORNERS", (0,0), (-1,-1), 4),
       ("TOPPADDING",    (0,0),(-1,-1), 7),
       ("BOTTOMPADDING", (0,0),(-1,-1), 7),
       ("LEFTPADDING",   (0,0),(-1,-1), 10),
   ]))
   return t
def bullet(text):
   return Paragraph(f"• {text}", bullet_s)
def numbered(i, text):
   return Paragraph(f"{i}. {text}", bullet_s)
def verify(text):
   return Paragraph(f"✅ {text}", verify_s)
def reflect(i, text):
   return Paragraph(f"{i}. {text}", reflect_s)
def code_block(lines):
   text = "<br/>".join(lines)
   t = Table([[Paragraph(text, code_s)]], colWidths=[W])
   t.setStyle(TableStyle([
       ("BACKGROUND", (0,0),(-1,-1), CODE),
       ("BOX",        (0,0),(-1,-1), 0.5, MGRAY),
       ("LEFTLINE",   (0,0),(0,-1),  3,   BLUE),
       ("TOPPADDING", (0,0),(-1,-1), 6),
       ("BOTTOMPADDING",(0,0),(-1,-1),6),
       ("LEFTPADDING",(0,0),(-1,-1), 10),
   ]))
   return t
def think_box(text):
   t = Table([[
       Paragraph("💭 Think:", think_lbl),
       Paragraph(text, think_s)
   ]], colWidths=[18*mm, W-18*mm])
   t.setStyle(TableStyle([
       ("BACKGROUND",    (0,0),(-1,-1), colors.HexColor("#FFFBF0")),
       ("LEFTLINE",      (0,0),(0,-1),  3, ORG),
       ("TOPPADDING",    (0,0),(-1,-1), 7),
       ("BOTTOMPADDING", (0,0),(-1,-1), 7),
       ("LEFTPADDING",   (0,0),(-1,-1), 8),
       ("VALIGN",        (0,0),(-1,-1), "TOP"),
   ]))
   return t
def flow_box(steps):
   lines = " → ".join(steps)
   t = Table([[Paragraph(lines, S("flow", fontName="Helvetica", fontSize=9.5, leading=14, textColor=DTEXT))]], colWidths=[W])
   t.setStyle(TableStyle([
       ("BACKGROUND",    (0,0),(-1,-1), colors.HexColor("#F0F7FF")),
       ("BOX",           (0,0),(-1,-1), 0.5, BLUE),
       ("TOPPADDING",    (0,0),(-1,-1), 8),
       ("BOTTOMPADDING", (0,0),(-1,-1), 8),
       ("LEFTPADDING",   (0,0),(-1,-1), 10),
   ]))
   return t
def lc_box(num, name, link, hint):
   t = Table([[
       Paragraph(f"<b>#{num}</b> — {name}<br/><font color='#2E75B6'>{link}</font><br/><i>Hint: {hint}</i>", lc_s)
   ]], colWidths=[W])
   t.setStyle(TableStyle([
       ("BACKGROUND",    (0,0),(-1,-1), colors.HexColor("#E8F4FD")),
       ("BOX",           (0,0),(-1,-1), 0.5, BLUE),
       ("LEFTLINE",      (0,0),(0,-1),  3, GREEN),
       ("TOPPADDING",    (0,0),(-1,-1), 8),
       ("BOTTOMPADDING", (0,0),(-1,-1), 8),
       ("LEFTPADDING",   (0,0),(-1,-1), 10),
   ]))
   return t
def tomorrow_box(text):
   t = Table([[Paragraph(f"📅  Tomorrow — {text}", tmrw_s)]], colWidths=[W])
   t.setStyle(TableStyle([
       ("BACKGROUND",    (0,0),(-1,-1), colors.HexColor("#F5F5F5")),
       ("BOX",           (0,0),(-1,-1), 0.5, MGRAY),
       ("TOPPADDING",    (0,0),(-1,-1), 7),
       ("BOTTOMPADDING", (0,0),(-1,-1), 7),
       ("LEFTPADDING",   (0,0),(-1,-1), 10),
   ]))
   return t
def week_cover(num, title, dsa, ai, project):
   t = Table([[
       Paragraph(f"WEEK {num}", S("wn", fontName="Helvetica-Bold", fontSize=13, textColor=colors.HexColor("#BDD7EE"))),
   ],[
       Paragraph(title, week_title),
   ],[
       Paragraph(f"📘 DSA: {dsa}   🤖 AI: {ai}   🔨 Project: {project}",
                 S("winfo", fontName="Helvetica", fontSize=9.5, textColor=colors.HexColor("#BDD7EE")))
   ]], colWidths=[W])
   t.setStyle(TableStyle([
       ("BACKGROUND",    (0,0),(-1,-1), NAV),
       ("TOPPADDING",    (0,0),(-1,-1), 6),
       ("BOTTOMPADDING", (0,0),(-1,-1), 6),
       ("LEFTPADDING",   (0,0),(-1,-1), 12),
   ]))
   return t
def day_header(week, day, title):
   t = Table([[
       Paragraph(f"W{week} · D{day}  —  {title}  <font size=9>⏱ 2 hours total</font>", day_title)
   ]], colWidths=[W])
   t.setStyle(TableStyle([
       ("BACKGROUND",    (0,0),(-1,-1), BLUE),
       ("TOPPADDING",    (0,0),(-1,-1), 8),
       ("BOTTOMPADDING", (0,0),(-1,-1), 8),
       ("LEFTPADDING",   (0,0),(-1,-1), 12),
   ]))
   return t
# ══════════════════════════════════════════════
#  CURRICULUM DATA
# ══════════════════════════════════════════════
curriculum = [
# ── WEEK 1 ──────────────────────────────────
{ "week":1, "day":1, "title":"Setup & First API Call",
 "b1_concept":"Arrays & HashMaps",
 "b1_bullets":[
   "Array = ordered list, O(1) index access, O(n) search — Python list",
   "HashMap = key-value store, O(1) average lookup — Python dict",
   "Array stores things in order; HashMap finds things instantly by key",
 ],
 "b1_code":["chat_history = []          # Array","cache = {}                 # HashMap","cache['what is array'] = 'ordered list'  # O(1) insert","cache.get('what is array')               # O(1) lookup"],
 "b1_think":"Your chatbot needs to remember last 5 messages — Array or HashMap, and why?",
 "b2_num":"1","b2_name":"Two Sum",
 "b2_link":"leetcode.com/problems/two-sum",
 "b2_why":"Forces you to think Array (brute force O(n²)) vs HashMap (optimized O(n)) — exact same decision you make building chatbot cache",
 "b2_hint":"Store each number in a HashMap as you scan; check if complement already exists — one pass, no nested loop",
 "b3_concept":"Groq API + LLM Message Format",
 "b3_bullets":[
   "Groq is a free LLM API — no credit card, fast response, same interface as OpenAI",
   "API takes a list of messages — that list IS an Array, each message IS a HashMap",
   "Sign up at groq.com → get free API key in 2 minutes",
 ],
 "b3_code":["messages = [                              # Array","    {'role':'system','content':'...'},  # HashMap","    {'role':'user',  'content':'...'},  # HashMap","]"],
 "b4_what":"CLI chatbot using Arrays and HashMaps from Block 1",
 "b4_flow":["user types","append to chat_history list (Array!)","check cache dict (HashMap!)","cached? → return instantly","not cached? → call Groq → store in cache → return reply"],
 "b4_tasks":["Save as week1_day1.py","Get Groq API key → store in .env file","Build chat loop: input → store in list → call Groq → print reply","Add caching: same question twice → return cached answer, skip API call"],
 "b4_verify":["Chatbot replies to any question","Same question twice returns cached answer instantly","chat_history list grows with each message","API key not hardcoded in file"],
 "reflect":["Where exactly did you use an Array in your code?","Where exactly did you use a HashMap?","What happens if cache grows too large — how would you fix it? 🎯"],
 "tomorrow":"Day 2 — Stacks & Queues → conversation memory with token limit",
},
{ "week":1, "day":2, "title":"Conversation Memory",
 "b1_concept":"Stacks & Queues",
 "b1_bullets":[
   "Stack = LIFO (Last In First Out) — like a pile of plates, Python list with append/pop",
   "Queue = FIFO (First In First Out) — like a line at a store, Python deque",
   "Your chatbot needs a Queue for chat history — oldest messages leave first when full",
 ],
 "b1_code":["from collections import deque","queue = deque(maxlen=10)  # auto-drops oldest when full","queue.append('msg1')","queue.append('msg2')","# stack","stack = []","stack.append('step1')","stack.pop()  # removes last"],
 "b1_think":"Chat history has a token limit. Would Stack or Queue handle this better — which removes the right end?",
 "b2_num":"20","b2_name":"Valid Parentheses",
 "b2_link":"leetcode.com/problems/valid-parentheses",
 "b2_why":"Classic Stack problem — same push/pop logic you use to track prompt chain steps in your chatbot",
 "b2_hint":"Push opening brackets onto stack; when closing bracket found, pop and check if it matches",
 "b3_concept":"Conversation History & Token Management",
 "b3_bullets":[
   "LLMs have context limits — you can't send infinite history",
   "Solution: trim oldest messages when token count exceeds budget",
   "Token ≈ word/4 chars — count tokens before every API call",
 ],
 "b3_code":["chat_history = deque()  # Queue from DSA!","def trim_to_budget(history, max_tokens=3000):","    while token_count(history) > max_tokens:","        history.popleft()  # remove oldest message"],
 "b4_what":"Chatbot with smart memory that trims itself when it gets too long",
 "b4_flow":["user types","append to deque (Queue!)","count total tokens in history","over limit? → popleft() oldest messages","send trimmed history to Groq","get reply → append to history"],
 "b4_tasks":["Save as week1_day2.py","Replace plain list with deque for chat_history","Add token counting function (len(text)//4 is fine)","Add trim_to_budget() that pops oldest when over limit","Test: have a long conversation, verify old messages disappear"],
 "b4_verify":["Long conversation doesn't crash or send too many tokens","Oldest messages removed first (not newest)","System prompt always stays — never trimmed","Token count stays under your budget"],
 "reflect":["Why deque instead of a plain list for chat history?","What happens if you pop from the wrong end?","Should the system prompt ever be trimmed — how do you protect it? 🎯"],
 "tomorrow":"Day 3 — Linked Lists → build a prompt chain that links AI calls together",
},
{ "week":1, "day":3, "title":"Prompt Chaining",
 "b1_concept":"Linked Lists",
 "b1_bullets":[
   "Linked List = chain of nodes, each pointing to next — no random access, only sequential",
   "Each node has data + a pointer to next node",
   "Your prompt chain IS a linked list — each LLM response feeds into the next call",
 ],
 "b1_code":["class Node:","    def __init__(self, data):","        self.data = data","        self.next = None","# Chain: question → answer → refine → final","node1 = Node('raw answer')","node2 = Node('refined answer')","node1.next = node2"],
 "b1_think":"In your prompt chain, if step 2 fails should you retry from step 1 or skip to step 3? How does linked list help decide?",
 "b2_num":"206","b2_name":"Reverse Linked List",
 "b2_link":"leetcode.com/problems/reverse-linked-list",
 "b2_why":"Forces you to think about pointer manipulation — same concept as chaining LLM calls where output of one becomes input of next",
 "b2_hint":"Use three pointers: prev, curr, next — update one at a time as you traverse",
 "b3_concept":"Prompt Chaining (Multi-step LLM Calls)",
 "b3_bullets":[
   "Instead of one LLM call, chain multiple — output of call 1 becomes input of call 2",
   "Improves quality: first call generates, second call refines",
   "Use a stack to track each step — so you can debug or rollback",
 ],
 "b3_code":["stack = []  # track chain steps","# Step 1: generate","r1 = ollama.chat(model=model, messages=[{'role':'user','content':prompt}])","base = r1['message']['content']","stack.append(base)","# Step 2: refine","r2 = ollama.chat(model=model, messages=[{'role':'user','content':f'refine: {base}'}])","refined = r2['message']['content']","stack.append(refined)"],
 "b4_what":"Two-step prompt chain where first call generates answer, second call refines it",
 "b4_flow":["user question","build prompt with context","call Groq → get base answer → push to stack","call Groq again with 'refine this: {base}'","check refined answer quality","if bad → pop stack → use base answer instead","return best answer"],
 "b4_tasks":["Save as week1_day3.py","Add stack = [] to ChatMemory","In chain(): call Groq twice — generate then refine","Push each result to stack","If refined is too short or has 'error' → pop and use base"],
 "b4_verify":["Two API calls happen per question","Stack has 2 items after each response","Bad refinement falls back to base answer","Final answer is better quality than single call"],
 "reflect":["When would chaining 3 calls be better than 2?","What's the cost of chaining — tokens, latency?","Could you chain in a loop until quality is good enough — what's the risk? 🎯"],
 "tomorrow":"Week 2, Day 1 — Embeddings & Semantic Search → your chatbot finds relevant info",
},
# ── WEEK 2 ──────────────────────────────────
{ "week":2, "day":1, "title":"Embeddings & Semantic Search",
 "b1_concept":"Searching & Binary Search",
 "b1_bullets":[
   "Linear search = check every item O(n) — slow for large data",
   "Binary search = split in half each time O(log n) — requires sorted data",
   "Semantic search is smarter: finds meaning, not just exact keyword match",
 ],
 "b1_code":["# Binary search — O(log n)","def binary_search(arr, target):","    lo, hi = 0, len(arr)-1","    while lo <= hi:","        mid = (lo+hi)//2","        if arr[mid] == target: return mid","        elif arr[mid] < target: lo = mid+1","        else: hi = mid-1","    return -1"],
 "b1_think":"Binary search needs sorted data. How would you 'sort' documents for semantic search — what does sorted even mean for text?",
 "b2_num":"704","b2_name":"Binary Search",
 "b2_link":"leetcode.com/problems/binary-search",
 "b2_why":"Core search pattern — understanding O(log n) vs O(n) is exactly why vector search beats keyword scanning in RAG",
 "b2_hint":"Always update lo or hi past mid — never set lo=mid or you risk infinite loop",
 "b3_concept":"Embeddings & Vector Similarity",
 "b3_bullets":[
   "Embedding = converting text into a list of numbers (vector) that captures meaning",
   "Similar meaning → vectors are close together in space (high cosine similarity)",
   "Ollama can generate embeddings locally for free: ollama.embeddings()",
 ],
 "b3_code":["import ollama","response = ollama.embeddings(model='qwen2.5', prompt='what is a graph?')","vector = response['embedding']  # list of ~4096 floats","# similar questions → similar vectors → can find related content"],
 "b4_what":"Function that takes user question, embeds it, finds most similar document chunk",
 "b4_flow":["load document text","split into chunks (size=200, overlap=50)","embed each chunk → store vectors","user asks question","embed question → compare to all chunk vectors","return top 3 most similar chunks"],
 "b4_tasks":["Save as week2_day1.py","Write chunk_text(text, size=200, overlap=50)","Write embed(text) using ollama.embeddings()","Write cosine_similarity(v1, v2)","Write find_top_k(query, chunks, k=3) using your similarity function"],
 "b4_verify":["Chunks overlap correctly — no content lost","Embedding returns a list of floats","Similar questions return similar chunks","Unrelated questions return low similarity scores"],
 "reflect":["Why overlap chunks instead of clean splits?","What happens if chunk size is too small? Too large?","Cosine similarity vs dot product — when does it matter? 🎯"],
 "tomorrow":"Day 2 — ChromaDB → store and retrieve embeddings with a real vector database",
},
{ "week":2, "day":2, "title":"ChromaDB Vector Store",
 "b1_concept":"Hash Tables (Deep Dive)",
 "b1_bullets":[
   "Hash Table is what powers ChromaDB's fast retrieval under the hood",
   "Hashing maps a key to a fixed-size index — O(1) average lookup",
   "Collision handling (chaining/open addressing) keeps it reliable",
 ],
 "b1_code":["# Python dict is a hash table","d = {}","d['graph'] = [0.1, 0.4, ...]  # hash('graph') → bucket → store","d['graph']                      # hash('graph') → same bucket → O(1) get"],
 "b1_think":"ChromaDB stores millions of vectors. Why is hashing better than scanning all vectors linearly for every query?",
 "b2_num":"146","b2_name":"LRU Cache",
 "b2_link":"leetcode.com/problems/lru-cache",
 "b2_why":"LRU = Least Recently Used — same eviction strategy your chatbot uses when response_cache is full (OrderedDict)",
 "b2_hint":"Use OrderedDict — move accessed items to end, pop from front when over capacity",
 "b3_concept":"ChromaDB — Persistent Vector Database",
 "b3_bullets":[
   "ChromaDB stores embeddings on disk — persists between runs",
   "get_or_create_collection — safely loads existing or makes new",
   "Query returns top-k most similar documents automatically",
 ],
 "b3_code":["import chromadb","from chromadb.config import Settings","client = chromadb.Client(Settings(persist_directory='./vectorstore'))","col = client.get_or_create_collection('dsa_docs')","col.add(documents=chunks, embeddings=embeddings, ids=ids)","result = col.query(query_embeddings=[q_vec], n_results=3)","top_chunks = result['documents'][0]"],
 "b4_what":"VectorStore class that saves chunks to ChromaDB and retrieves relevant ones",
 "b4_flow":["load document","create chunks","embed all chunks","store in ChromaDB (persists to disk)","on next run: skip embedding — load existing","user queries → embed query → ChromaDB returns top 3"],
 "b4_tasks":["Save as week2_day2.py","Build VectorStore class with __init__, add_chunks, search methods","In add_chunks: check if collection already has data — skip if yes (Loading_existing)","In search: query ChromaDB and return top documents","Test: run twice — second run should print 'Loading_existing'"],
 "b4_verify":["First run builds and saves vector store","Second run loads existing — no re-embedding","Search returns relevant chunks for DSA questions","Unrelated query returns low-relevance results"],
 "reflect":["Why check collection.count() before adding chunks?","What breaks if you re-add same chunks every run?","When would you want to rebuild the vector store from scratch? 🎯"],
 "tomorrow":"Day 3 — Tool Routing → chatbot decides which tool to use based on user input",
},
{ "week":2, "day":3, "title":"Tool Routing & RAG Pipeline",
 "b1_concept":"Sorting & Priority",
 "b1_bullets":[
   "Sorting = arranging data by a key — O(n log n) for most algorithms",
   "Priority Queue = always gives you the highest priority item first",
   "RAG ranking = sort retrieved chunks by relevance score before using them",
 ],
 "b1_code":["# Sort chunks by relevance score","chunks = [('graph def', 0.9), ('array def', 0.4), ('tree def', 0.7)]","chunks.sort(key=lambda x: x[1], reverse=True)","# → [('graph def', 0.9), ('tree def', 0.7), ('array def', 0.4)]"],
 "b1_think":"Your route_tool checks conditions in a fixed order. What if two conditions match — which wins, and is that the right behavior?",
 "b2_num":"347","b2_name":"Top K Frequent Elements",
 "b2_link":"leetcode.com/problems/top-k-frequent-elements",
 "b2_why":"Finding top-k by frequency = same logic as finding top-k relevant chunks by similarity score in RAG",
 "b2_hint":"Use a HashMap for frequency count, then heap or sort to get top k",
 "b3_concept":"Tool Routing — Agent Decision Making",
 "b3_bullets":[
   "Instead of always calling LLM, route to the right tool first",
   "Math question → calculator, Definition question → dict, History → memory, else → RAG",
   "Tool router is if/elif logic — Week 4 upgrades it to a graph",
 ],
 "b3_code":["def route_tool(user_input, memory):","    if '**' in user_input or any(s in user_input for s in '+-*/'):","        return 'calculate', calculate(user_input)","    if any(k in user_input.lower() for k in ['what is','define']):","        return 'define', define_term(user_input)","    if any(k in user_input.lower() for k in ['history','discuss']):","        return 'history', get_history(memory)","    return 'search', search_document(user_input, memory)"],
 "b4_what":"Full RAG pipeline: route → retrieve → prompt → chain → reply",
 "b4_flow":["user question","route_tool() decides: calculate / define / history / search","if search: embed query → ChromaDB → top 3 chunks","build prompt: context + question","call Groq (step 1: generate, step 2: refine)","return refined answer"],
 "b4_tasks":["Save as week2_day3.py","Combine VectorStore + ChatMemory + route_tool into one file","Add define_term dict with 5 DSA terms","Add calculate() using eval with safety check","Test all 4 routes: math, define, history, RAG search"],
 "b4_verify":["'2**10' → 1024 (calculate route)","'what is graph' → definition (define route)","'what we discussed' → history (history route)","'explain binary search' → RAG search → LLM answer"],
 "reflect":["Which route gets triggered most in testing?","What happens when route_tool picks the wrong tool?","How would you add a 5th tool — what's the cleanest way? 🎯"],
 "tomorrow":"Week 3, Day 1 — Graph theory → redesign router as a graph of decisions",
},
# ── WEEK 3 ──────────────────────────────────
{ "week":3, "day":1, "title":"Graph Theory & Router as a Graph",
 "b1_concept":"Graphs — Nodes, Edges, Traversal",
 "b1_bullets":[
   "Graph = set of nodes connected by edges — can be directed or undirected",
   "Adjacency list = HashMap where each node maps to list of neighbors",
   "BFS (Breadth First) = visit level by level using Queue; DFS (Depth First) = go deep using Stack/recursion",
 ],
 "b1_code":["TOOL_GRAPH = {","    'start':         ['math_check','keyword_check','history_check','default'],","    'math_check':    ['calculate'],","    'keyword_check': ['define'],","    'history_check': ['history'],","    'default':       ['search']","}","# BFS traversal","from collections import deque","queue = deque(TOOL_GRAPH['start'])"],
 "b1_think":"Your current if/elif router is linear. What breaks if you add 10 more tools — and how does a graph fix that?",
 "b2_num":"200","b2_name":"Number of Islands",
 "b2_link":"leetcode.com/problems/number-of-islands",
 "b2_why":"BFS/DFS on a grid — exact same traversal logic you use to walk your tool routing graph",
 "b2_hint":"Use BFS from each unvisited '1' cell — mark visited as '0' to avoid revisiting",
 "b3_concept":"BFS-Based Tool Router",
 "b3_bullets":[
   "Replace if/elif chain with a graph of tool nodes",
   "BFS traverses graph — checks each node in order, stops when a tool matches",
   "Adding new tools = add a node + edge to graph, no touching existing logic",
 ],
 "b3_code":["from collections import deque","def route_tool(user_input, memory):","    queue = deque(TOOL_GRAPH['start'])","    visited = set()","    while queue:","        node = queue.popleft()","        if node in visited: continue","        visited.add(node)","        name, result = check_node(node, user_input, memory)","        if name: return name, result","        for child in TOOL_GRAPH.get(node, []):","            if child not in visited: queue.append(child)","    return 'search', search_document(user_input, memory)"],
 "b4_what":"Replace your if/elif route_tool with BFS graph traversal",
 "b4_flow":["define TOOL_GRAPH as adjacency list","BFS starts at 'start' node","dequeue node → check_node() → does user input match?","yes → return tool result","no → add children to queue → continue BFS","fallback to search if nothing matched"],
 "b4_tasks":["Save as week3_day1.py","Define TOOL_GRAPH dict (adjacency list)","Write check_node(node, user_input, memory) with conditions per node","Replace old route_tool with BFS version","Verify all 4 routes still work exactly as before"],
 "b4_verify":["All 4 routes still work (math, define, history, search)","Adding a new tool only requires adding to TOOL_GRAPH — not touching other code","Visited set prevents infinite loops","BFS order matches expected priority"],
 "reflect":["Did BFS change which tool gets priority vs old if/elif?","What if two nodes both match — which wins in BFS?","When would DFS routing be better than BFS? 🎯"],
 "tomorrow":"Day 2 — DFS Agent Loop → chatbot retries with fallback tools when first result is weak",
},
{ "week":3, "day":2, "title":"DFS Agent Loop",
 "b1_concept":"DFS — Depth First Search",
 "b1_bullets":[
   "DFS = go deep into one path completely before trying another",
   "Uses a visited set to avoid revisiting — same as BFS but goes deep first",
   "In your agent: try one tool fully → if result weak → go deeper to next tool",
 ],
 "b1_code":["def dfs(graph, start, visited=None):","    if visited is None: visited = set()","    visited.add(start)","    print(start)","    for neighbor in graph[start]:","        if neighbor not in visited:","            dfs(graph, neighbor, visited)"],
 "b1_think":"Your agent tries tools one by one. When should it stop retrying — after 2 failures? 3? What's the right max depth?",
 "b2_num":"133","b2_name":"Clone Graph",
 "b2_link":"leetcode.com/problems/clone-graph",
 "b2_why":"DFS with visited dict — same structure as your agent loop's visited_tools set that prevents calling the same tool twice",
 "b2_hint":"Use a HashMap {original_node: cloned_node} as visited — if already cloned, return it directly",
 "b3_concept":"Agent Loop — Self-Deciding Fallback",
 "b3_bullets":[
   "Instead of one tool call → stop, agent loops until it gets a good enough result",
   "Checks result quality after each tool — if weak, tries next tool as fallback",
   "Max depth prevents infinite loop — agent gives up after 3 tries",
 ],
 "b3_code":["def agent_loop(self, user_, route_tool, max_depth=3):","    visited_tools = set()  # DFS visited!","    depth = 0","    while depth < max_depth:","        tool_name, result = route_tool(user_, self)","        if tool_name in visited_tools: break","        visited_tools.add(tool_name)","        depth += 1","        if self._is_good_result(result): return tool_name, result","        # weak result → try search as fallback","    return tool_name, result"],
 "b4_what":"Agent loop with DFS fallback — tries harder before giving up",
 "b4_flow":["call route_tool","check result quality (_is_good_result)","good → return immediately","weak → add to visited_tools → try search fallback","search also weak → return honestly 'topic not in document'","max depth hit → stop"],
 "b4_tasks":["Save as week3_day2.py","Add _is_good_result(result) that checks length, 'not found' phrases","Add agent_loop() with visited set and max_depth","Update chain() to call agent_loop instead of single route_tool","Test: 'what is binary search' → not in definitions → should fall to RAG"],
 "b4_verify":["'what is graph' → define route, returns immediately (1 iteration)","'what is binary search' → define fails → falls to RAG (2 iterations)","'explain quantum physics' → RAG weak → returns honest message","Stack has correct number of entries after each chain"],
 "reflect":["How many iterations did your agent use for each test case?","Did max_depth=3 ever get hit — what triggered it?","Should calculate ever trigger fallback — why or why not? 🎯"],
 "tomorrow":"Day 3 — Multi-tool chaining → one question triggers two tools, answers combined",
},
{ "week":3, "day":3, "title":"Multi-Tool Chaining",
 "b1_concept":"Dynamic Programming — Memoization Preview",
 "b1_bullets":[
   "DP = breaking problem into subproblems, solving each once, storing results",
   "Memoization = cache subproblem results — never solve same thing twice",
   "Your response_cache IS memoization — same question never hits API twice",
 ],
 "b1_code":["from functools import lru_cache","@lru_cache(maxsize=128)","def fib(n):","    if n <= 1: return n","    return fib(n-1) + fib(n-2)","# Without cache: O(2^n)  With cache: O(n)"],
 "b1_think":"Your chatbot caches full question→answer pairs. Could you cache partial results (just the retrieved chunks) separately — what's the benefit?",
 "b2_num":"70","b2_name":"Climbing Stairs",
 "b2_link":"leetcode.com/problems/climbing-stairs",
 "b2_why":"Classic memoization intro — teaches you to recognize overlapping subproblems, same pattern as caching LLM responses",
 "b2_hint":"fib(n) = fib(n-1) + fib(n-2) — store results in a dict, check before computing",
 "b3_concept":"Multi-Tool Chaining — Combining Results",
 "b3_bullets":[
   "One question can benefit from multiple tools — e.g. define + search + refine",
   "Chain results: tool1 output → feeds into tool2 prompt → final answer",
   "Different from agent loop: both tools run intentionally, not as fallback",
 ],
 "b3_code":["def multi_chain(self, user_, tools):","    results = []","    for tool_name in tools:","        _, output = TOOLS[tool_name](user_, self)","        if self._is_good_result(output):","            results.append(output)","    combined = '\n\n'.join(results)","    # send combined context to LLM for final answer","    return self._llm_synthesize(combined, user_)"],
 "b4_what":"Chatbot that combines define + RAG search results into one richer answer",
 "b4_flow":["user asks question","check define_term dict → get short definition if exists","embed query → ChromaDB → get top 3 chunks","combine: definition + chunks as context","send to Groq: 'using this context, answer the question fully'","return synthesized answer"],
 "b4_tasks":["Save as week3_day3.py","Add multi_chain() method that runs define + search sequentially","Combine results into one context string","Update chain() to use multi_chain when both tools return results","Test: 'explain graph traversal' → should use both define + RAG"],
 "b4_verify":["'what is graph' → gets definition AND document context","Single tool question still works normally","Combined context produces richer answer than either alone","No duplicate content in combined result"],
 "reflect":["Did combining tools actually improve answer quality?","What's the token cost of combining vs single tool?","When would you NOT want to combine — what's a bad combo? 🎯"],
 "tomorrow":"Week 4, Day 1 — Full project review + bug fixes before moving to production features",
},
# ── WEEK 4 ──────────────────────────────────
{ "week":4, "day":1, "title":"Project Review & Bug Fixes",
 "b1_concept":"Recap — All Structures Used So Far",
 "b1_bullets":[
   "Array (list) → chat_history stores messages in order",
   "HashMap (dict/OrderedDict) → response_cache for O(1) lookup",
   "Queue (deque) → chat_history with token trimming (FIFO)",
   "Stack (list) → prompt chain tracking (LIFO)",
   "Graph (dict of lists) → tool routing via BFS",
 ],
 "b1_code":["# Your project uses ALL of these:","chat_history = deque()       # Queue","response_cache = OrderedDict()  # HashMap (LRU)","stack = []                   # Stack","TOOL_GRAPH = {}              # Graph","embeddings = []              # Array"],
 "b1_think":"Looking at your full codebase — which data structure is doing the most work? Which one could you remove without breaking anything?",
 "b2_num":"242","b2_name":"Valid Anagram",
 "b2_link":"leetcode.com/problems/valid-anagram",
 "b2_why":"Revisit HashMap frequency counting — reinforces the pattern you use in token counting and cache key matching",
 "b2_hint":"Count character frequencies for both strings using Counter or a dict — compare the two dicts",
 "b3_concept":"Code Quality — Normalize, Cache Keys, Edge Cases",
 "b3_bullets":[
   "normalize() cleans user input — removes punctuation, lowercases — for consistent cache keys",
   "Bug: normalizing before routing vs after causes mismatches in history and cache",
   "Fix: normalize only for cache key, store original text in chat_history",
 ],
 "b3_code":["# WRONG: normalize before everything","normalized = self.normalize(user_)","self.chat_history.append({'role':'user','content':normalized})","# RIGHT: normalize only for cache key","self.chat_history.append({'role':'user','content':user_})  # original","cache_key = self.normalize(user_)  # normalized for cache only"],
 "b4_what":"Audit and fix all known bugs in your current codebase",
 "b4_flow":["run chatbot with 5 test inputs","check: history shows correct messages","check: cache hit on repeated questions","check: new document content gets indexed","check: get_history returns full conversation","fix each bug found"],
 "b4_tasks":["Save as week4_day1.py (clean version)","Fix normalize bug: store original in history, normalize only for cache","Fix get_history: show all messages not just last 3","Fix ChromaDB: add new chunks that don't already exist (check IDs)","Run all 4 route tests and confirm clean output"],
 "b4_verify":["'what we discuss' shows full conversation history","Same question twice → cache hit message printed","New content in document file gets picked up on next run","No duplicate chunks in ChromaDB"],
 "reflect":["Which bug was hardest to find and why?","How would you write a test to catch the normalize bug automatically?","What would break first if you scaled this to 10,000 documents? 🎯"],
 "tomorrow":"Day 2 — Graph BFS router upgrade → cleaner, extensible tool routing",
},
{ "week":4, "day":2, "title":"BFS Router Upgrade",
 "b1_concept":"BFS Deep Dive — Level Order Traversal",
 "b1_bullets":[
   "BFS visits all nodes at current level before going deeper",
   "Uses a Queue — enqueue neighbors, dequeue and process one by one",
   "Level order = first all direct neighbors, then their neighbors",
 ],
 "b1_code":["from collections import deque","def bfs(graph, start):","    visited = set([start])","    queue = deque([start])","    while queue:","        node = queue.popleft()","        print(node)","        for neighbor in graph[node]:","            if neighbor not in visited:","                visited.add(neighbor)","                queue.append(neighbor)"],
 "b1_think":"In your TOOL_GRAPH, 'start' has 4 neighbors. BFS visits them all before going deeper. Is that the right priority order for your chatbot?",
 "b2_num":"102","b2_name":"Binary Tree Level Order Traversal",
 "b2_link":"leetcode.com/problems/binary-tree-level-order-traversal",
 "b2_why":"Classic BFS on tree — same Queue pattern you use to traverse TOOL_GRAPH level by level",
 "b2_hint":"Use a deque, enqueue root, then for each level enqueue all children before processing next level",
 "b3_concept":"Extensible Graph Router with check_node",
 "b3_bullets":[
   "Each node in TOOL_GRAPH has a matching check_node() condition",
   "Adding new tool = add node to graph + add condition to check_node — no other changes",
   "This is the Open/Closed principle: open for extension, closed for modification",
 ],
 "b3_code":["def check_node(node, user_input, memory):","    u = user_input.lower()","    if node == 'math_check':","        if '**' in user_input or any(s in user_input for s in '+-*/'):","            return 'calculate', TOOLS['calculate'](user_input)","    if node == 'keyword_check':","        if any(k in u for k in ['what is','define']):","            term = u.replace('what is','').replace('define','').strip()","            return 'define', TOOLS['define'](term)","    # ... other nodes","    return None, None"],
 "b4_what":"Clean, extensible BFS router replacing old if/elif chain",
 "b4_flow":["define TOOL_GRAPH with all nodes","BFS starts at 'start'","dequeue node → check_node() matches?","yes → return result","no → add children to queue","repeat until queue empty → fallback to search"],
 "b4_tasks":["Save as week4_day2.py","Define complete TOOL_GRAPH with 5 nodes","Write check_node() covering all conditions","Implement BFS route_tool using deque + visited set","Add a 6th tool 'summarize' — only add to graph + check_node"],
 "b4_verify":["All existing routes still pass","New 'summarize' tool works when triggered","Adding summarize required no changes to BFS loop itself","Visited set prevents any node from running twice"],
 "reflect":["Did the graph structure make adding 'summarize' easier than old if/elif?","What's the time complexity of your BFS router?","How would you make TOOL_GRAPH configurable from a JSON file? 🎯"],
 "tomorrow":"Day 3 — DFS Agent Loop with fallback → chatbot retries smarter",
},
{ "week":4, "day":3, "title":"DFS Agent Loop with Smart Fallback",
 "b1_concept":"DFS vs BFS — When to Use Which",
 "b1_bullets":[
   "BFS = good for finding shortest path, level-by-level exploration (your router)",
   "DFS = good for exploring one path fully before backtracking (your agent loop)",
   "Agent loop uses DFS: try tool → weak? → go deeper into fallback → weak? → give up",
 ],
 "b1_code":["# DFS iterative using explicit stack","def dfs_iterative(graph, start):","    stack = [start]","    visited = set()","    while stack:","        node = stack.pop()  # LIFO — go deep","        if node in visited: continue","        visited.add(node)","        print(node)","        for neighbor in graph[node]:","            stack.append(neighbor)"],
 "b1_think":"BFS router gives first match quickly. DFS agent loop explores deeply. Could you combine them — BFS to pick tool, DFS to retry on failure?",
 "b2_num":"133","b2_name":"Clone Graph",
 "b2_link":"leetcode.com/problems/clone-graph",
 "b2_why":"DFS with visited HashMap — exact pattern of agent_loop visited_tools set preventing same tool from running twice",
 "b2_hint":"visited dict maps original→clone; if node already in dict return clone directly without re-processing",
 "b3_concept":"Agent Loop — Quality Check & Fallback",
 "b3_bullets":[
   "_is_good_result() is your quality gate — checks length, error phrases, 'not found'",
   "Agent tries tool → weak result → tries search → still weak → returns honest message",
   "Max depth=3 prevents runaway loops — agent gives up gracefully",
 ],
 "b3_code":["def _is_good_result(self, result):","    if not result: return False","    bad = ['not found','no context','definition not found','error']","    if any(b in result.lower() for b in bad): return False","    if len(result.strip()) < 20: return False","    return True"],
 "b4_what":"Agent loop that DFS-retries with fallback tools when first result is weak",
 "b4_flow":["call BFS route_tool → get tool + result","_is_good_result? → yes → return","no → add to visited_tools → try search fallback","search result good? → return","both weak → return 'topic not covered in document'","max depth hit → stop regardless"],
 "b4_tasks":["Save as week4_day3.py","Add _is_good_result() with all quality checks","Add agent_loop() with visited set and max_depth=3","Update chain() to call agent_loop instead of route_tool directly","Test: query not in document → should get honest fallback message"],
 "b4_verify":["'what is graph' → direct define result (1 iteration)","'explain merge sort' (not in doc) → define weak → search weak → honest message","'2**8' → calculate returns immediately, no loop","Stack entries reflect actual number of chain steps taken"],
 "reflect":["How many iterations for each of your 4 test cases?","Did max_depth ever get hit — what caused it?","Is _is_good_result() too strict or too lenient — how would you tune it? 🎯"],
 "tomorrow":"Day 4 — Multi-tool chaining → combine define + RAG for richer answers",
},
{ "week":4, "day":4, "title":"Multi-Tool Chaining & Combined Answers",
 "b1_concept":"Dynamic Programming — Overlapping Subproblems",
 "b1_bullets":[
   "DP = recognize subproblems that repeat → solve once → reuse answer",
   "Two properties needed: optimal substructure + overlapping subproblems",
   "Your multi-tool chain IS DP thinking: define gives part of answer, RAG gives rest — combine once",
 ],
 "b1_code":["# Fibonacci with memoization","memo = {}","def fib(n):","    if n in memo: return memo[n]  # reuse!","    if n <= 1: return n","    memo[n] = fib(n-1) + fib(n-2)","    return memo[n]","# O(2^n) → O(n) with memoization"],
 "b1_think":"In multi-tool chaining, you call define + search for every question. Could you cache the 'define' result separately from 'search' — what's the benefit?",
 "b2_num":"70","b2_name":"Climbing Stairs",
 "b2_link":"leetcode.com/problems/climbing-stairs",
 "b2_why":"Simplest DP problem — teaches memoization pattern you apply to caching partial results in multi-tool chain",
 "b2_hint":"Ways to reach step n = ways(n-1) + ways(n-2) — store each in a dict before recursing",
 "b3_concept":"Synthesizing Multiple Tool Results",
 "b3_bullets":[
   "Multi-chain: run define + search both → combine into one rich context",
   "Send combined context to LLM: 'using both sources, give a complete answer'",
   "Better than either alone: definition gives precision, RAG gives detail",
 ],
 "b3_code":["def multi_chain(self, user_):","    results = []","    # Tool 1: define","    _, defn = TOOLS['define'](user_, self)","    if self._is_good_result(defn): results.append(f'Definition: {defn}')","    # Tool 2: RAG search","    context = self.retrive_context(user_)","    if context != 'No Context Found': results.append(f'Document context:\n{context}')","    if not results: return 'Topic not covered in loaded document.'","    combined = '\n\n'.join(results)","    prompt = f'Using this info:\n{combined}\n\nAnswer: {user_}'","    r = ollama.chat(model=self.model, messages=[{'role':'user','content':prompt}])","    return r['message']['content']"],
 "b4_what":"Chatbot that combines define + RAG results into one synthesized answer",
 "b4_flow":["user asks question","run define_term → good result? → add to results list","run retrive_context → found? → add to results list","combine results into one context string","send to Groq: 'using this info, answer fully'","return synthesized response"],
 "b4_tasks":["Save as week4_day4.py","Add multi_chain() method to ChatMemory","Update chain() to call multi_chain() for search route","Keep calculate/history routes as direct returns — no multi_chain","Test: 'explain graph traversal' should use both define + RAG"],
 "b4_verify":["'explain graph' → gets definition + document context both used","'2**8' → still returns 1024 directly without multi_chain","'what we discuss' → history still works directly","Combined answer is visibly richer than single-tool answer"],
 "reflect":["Did combining tools improve the answer quality — by how much?","What's the extra token cost of multi_chain vs single tool?","When would you NOT combine — give a specific example from your tests 🎯"],
 "tomorrow":"Day 5 — Production cleanup: logging, stats, clean CLI interface",
},
]
# ══════════════════════════════════════════════
#  BUILD PDF
# ══════════════════════════════════════════════
def build_pdf(path):
   doc = SimpleDocTemplate(
       path, pagesize=A4,
       leftMargin=14*mm, rightMargin=14*mm,
       topMargin=14*mm, bottomMargin=14*mm
   )
   story = []
   # ── COVER PAGE ──
   story.append(sp(20))
   cover = Table([[Paragraph("DSA × AI Engineering", h_title)],
                  [Paragraph("Learn by Building — Full Curriculum", h_sub)],
                  [Paragraph("Week 1 → Week 4  •  Day-by-Day Playbook", h_sub)],
                  [sp(4)],
                  [Paragraph("Bobby · Lead AI Engineer · Mahindra",
                              S("cover_name", fontName="Helvetica", fontSize=10,
                                textColor=colors.HexColor("#BDD7EE"), alignment=TA_CENTER))],
                  ], colWidths=[W])
   cover.setStyle(TableStyle([
       ("BACKGROUND",    (0,0),(-1,-1), NAV),
       ("TOPPADDING",    (0,0),(-1,-1), 16),
       ("BOTTOMPADDING", (0,0),(-1,-1), 16),
       ("LEFTPADDING",   (0,0),(-1,-1), 20),
       ("RIGHTPADDING",  (0,0),(-1,-1), 20),
   ]))
   story.append(cover)
   story.append(sp(8))
   # progress table
   prog = Table([
       [Paragraph("✅  Week 1", S("p",fontName="Helvetica-Bold",fontSize=10,textColor=GREEN)),
        Paragraph("Arrays, HashMaps, Stacks, Queues, Linked Lists", base)],
       [Paragraph("✅  Week 2", S("p",fontName="Helvetica-Bold",fontSize=10,textColor=GREEN)),
        Paragraph("Embeddings, ChromaDB, Tool Routing, RAG Pipeline", base)],
       [Paragraph("✅  Week 3", S("p",fontName="Helvetica-Bold",fontSize=10,textColor=GREEN)),
        Paragraph("Graph BFS Router, DFS Agent Loop, Multi-Tool Chain", base)],
       [Paragraph("🔄  Week 4", S("p",fontName="Helvetica-Bold",fontSize=10,textColor=ORG)),
        Paragraph("Bug Fixes, BFS Upgrade, DFS Agent, Multi-Chain (In Progress)", base)],
   ], colWidths=[35*mm, W-35*mm])
   prog.setStyle(TableStyle([
       ("BOX",           (0,0),(-1,-1), 0.5, MGRAY),
       ("INNERGRID",     (0,0),(-1,-1), 0.3, MGRAY),
       ("BACKGROUND",    (0,0),(-1,-1), LGRAY),
       ("TOPPADDING",    (0,0),(-1,-1), 7),
       ("BOTTOMPADDING", (0,0),(-1,-1), 7),
       ("LEFTPADDING",   (0,0),(-1,-1), 10),
   ]))
   story.append(prog)
   story.append(PageBreak())
   current_week = None
   for d in curriculum:
       w, dy = d["week"], d["day"]
       # Week cover
       if w != current_week:
           current_week = w
           week_dsa = {1:"Arrays, HashMaps, Stacks, Queues, Linked Lists",
                       2:"Searching, Hash Tables, Sorting",
                       3:"Graphs BFS/DFS, DP Preview",
                       4:"Graph BFS/DFS Deep Dive, DP"}
           week_ai  = {1:"Groq API, Prompt Engineering, Chaining",
                       2:"Embeddings, ChromaDB, Tool Routing",
                       3:"BFS Router, Agent Loop, Multi-Chain",
                       4:"Bug Fixes, Upgraded Router, Agent, Synthesis"}
           week_proj= {1:"DSA AI Tutor Chatbot v1",
                       2:"RAG Pipeline with Tool Router",
                       3:"Graph-Routed Agent with Fallback",
                       4:"Production-Ready Chatbot"}
           story.append(week_cover(w, f"Week {w} — {week_proj[w]}",
                                   week_dsa[w], week_ai[w], week_proj[w]))
           story.append(sp(4))
       # Day header
       story.append(day_header(w, dy, d["title"]))
       story.append(sp(3))
       # ── BLOCK 1: DSA Concept ──
       story.append(block_header("DSA Concept"))
       story.append(sp(2))
       story.append(Paragraph(f"<b>Concept:</b> {d['b1_concept']}", concept_hdr))
       story.append(sp(1))
       for b in d["b1_bullets"]: story.append(bullet(b))
       story.append(sp(2))
       story.append(code_block(d["b1_code"]))
       story.append(sp(2))
       story.append(think_box(d["b1_think"]))
       story.append(sp(3))
       # ── BLOCK 2: DSA Problem ──
       story.append(block_header("DSA Problem"))
       story.append(sp(2))
       story.append(lc_box(d["b2_num"], d["b2_name"], d["b2_link"],d["b2_hint"]))
       story.append(sp(1))
       story.append(Paragraph(f"<b>Why this problem:</b> {d['b2_why']}", base))
       story.append(sp(3))
       # ── BLOCK 3: AI Concept ──
       story.append(block_header("AI Concept"))
       story.append(sp(2))
       story.append(Paragraph(f"<b>Concept:</b> {d['b3_concept']}", concept_hdr))
       story.append(sp(1))
       for b in d["b3_bullets"]: story.append(bullet(b))
       story.append(sp(2))
       story.append(code_block(d["b3_code"]))
       story.append(sp(3))
       # ── BLOCK 4: AI Project ──
       story.append(block_header("AI Project"))
       story.append(sp(2))
       story.append(Paragraph(f"<b>What you're building:</b> {d['b4_what']}", concept_hdr))
       story.append(sp(2))
       story.append(Paragraph("<b>The idea:</b>", bold_s))
       story.append(sp(1))
       story.append(flow_box(d["b4_flow"]))
       story.append(sp(2))
       story.append(Paragraph("<b>Your task:</b>", bold_s))
       for i, t in enumerate(d["b4_tasks"], 1): story.append(numbered(i, t))
       story.append(sp(2))
       story.append(Paragraph("<b>Verify:</b>", bold_s))
       for v in d["b4_verify"]: story.append(verify(v))
       story.append(sp(3))
       # ── REFLECT ──
       refl_t = Table([[Paragraph("🪞  Reflect  (5 min)",
                                   S("rh", fontName="Helvetica-Bold", fontSize=10, textColor=WHITE))]],
                       colWidths=[W])
       refl_t.setStyle(TableStyle([
           ("BACKGROUND",    (0,0),(-1,-1), PUR),
           ("TOPPADDING",    (0,0),(-1,-1), 6),
           ("BOTTOMPADDING", (0,0),(-1,-1), 6),
           ("LEFTPADDING",   (0,0),(-1,-1), 10),
       ]))
       story.append(refl_t)
       story.append(sp(1))
       for i, r in enumerate(d["reflect"], 1): story.append(reflect(i, r))
       story.append(sp(2))
       story.append(tomorrow_box(d["tomorrow"]))
       story.append(PageBreak())
   doc.build(story)
   print("PDF built successfully!")
build_pdf(r"E:\training\logger\DSA_AI_Curriculum.pdf")