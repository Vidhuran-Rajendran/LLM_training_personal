import requests

url = "http://127.0.0.1:8000/chat/stream"

data = {
    "user_id": "user1",
    "message": "Explain AVL"
}

with requests.post(url, json=data, stream=True) as r:
    for chunk in r.iter_content(chunk_size=None):
        if chunk:
            print(chunk.decode(), end="")