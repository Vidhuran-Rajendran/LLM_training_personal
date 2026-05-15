from fastapi import FastAPI, HTTPException
import time
from pydantic import BaseModel
from fastapi.responses import StreamingResponse
from memory_w6d2 import ChatMemory   # 🔁 change to your filename
import httpx

memory = ChatMemory()
memory.prepare_document("E:\\training\\LLM_training\\data\\final_clean_data.md",
                        size=500,
                        overlap=100)
test_cases = [
    {
        "question": "What is AVL tree?",
        "answer": "self-balancing binary search tree"
    },
    {
        "question": "Explain heap",
        "answer": "tree-based data structure"
    },
    {
        "question": "What is BST?",
        "answer": "binary search tree"
    }
]

def evaluate(bot, question, expected):
    response = bot.chat(question)

    print("\nQ:", question)
    print("Response:", response)

    if expected.lower() in response.lower():
        return 1
    return 0

def run_tests(bot):

    correct = 0

    for test in test_cases:
        correct += evaluate(bot, test["question"], test["answer"])

    total = len(test_cases)

    accuracy = (correct / total) * 100

    return {
        "score": f"{correct}/{total}",
        "accuracy": f"{accuracy:.2f}%"
    }

# ✅ create app
app = FastAPI()
sessions = {}
# ✅ initialize your RAG system
memory = ChatMemory()

# ✅ request schema
class ChatRequest(BaseModel):
    user_id: str
    message: str

# ✅ response schema
class ChatResponse(BaseModel):
    reply: str

def get_session(user_id):
    if user_id not in sessions:
        sessions[user_id] = ChatMemory()
    return sessions[user_id]

# ✅ main endpoint
# @app.post("/chat")
# async def chat_endpoint(req: ChatRequest):
#     try:
#         bot = get_session(req.user_id)
#         reply = bot.chat(req.message)
#         return{"reply": reply}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))


async def async_ollama_chat(model, messages):
    async with httpx.AsyncClient(timeout=60) as client:
        response = await client.post(
            "http://localhost:11434/api/chat",
            json={
                "model": model,
                "messages": messages,
                "stream": False
            }
            )
        return response.json()["message"]["content"]


@app.post("/chat")
async def chat_endpoint(req: ChatRequest):
    try:
        bot = get_session(req.user_id)

        # ✅ prepare messages (VERY IMPORTANT)
        messages = list(bot.chat_history) + [
            {"role": "user", "content": req.message}
        ]

        # ✅ async call
        reply = await async_ollama_chat(memory.model, messages)

        # ✅ store history
        bot.chat_history.append({"role": "user", "content": req.message})
        bot.chat_history.append({"role": "assistant", "content": reply})

        return {"reply": reply}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))