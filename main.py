from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from memory_week_5 import ChatMemory   # 🔁 change to your filename

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
        bot = ChatMemory()
        bot.prepare_document(
            path=r"E:\training\LLM_training\data\final_clean_data.md",
            size=500,
            overlap=100
        )
        sessions[user_id] = bot
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
    
@app.get("/evaluate")
async def evaluate_system():

    bot = get_session("test_user")   # fixed test session

    result = run_tests(bot)

    return result