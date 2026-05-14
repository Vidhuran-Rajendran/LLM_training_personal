from fastapi import FastAPI
from pydantic import BaseModel
from week_5.memory_week_5 import ChatMemory   # 🔁 change to your filename

# ✅ create app
app = FastAPI()

# ✅ initialize your RAG system
memory = ChatMemory()
memory.prepare_document(
    path="final_clean_dsa.md",   # your cleaned file ✅
    size=500,
    overlap=100
)

# ✅ request schema
class ChatRequest(BaseModel):
    message: str

# ✅ response schema
class ChatResponse(BaseModel):
    reply: str

# ✅ main endpoint
@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(req: ChatRequest):
    if req.message.lower() == "quit":
        return ChatResponse(reply="Goodbye!")

    reply = memory.chat(req.message)

    return ChatResponse(reply=reply)