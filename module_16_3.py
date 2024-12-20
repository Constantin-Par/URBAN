from fastapi import FastAPI

import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)


app = FastAPI()
users = {"1": "Имя: Example, возраст: 18"}


@app.get("/users")
async def get_users() -> dict:
    return users


@app.post("/user/{username}/{age}")
async def post_user(username: str, age: int) -> str:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} registered."


@app.put("/user/{user_id}/{username}/{age}")
async def put_user(user_id: str, username: str, age: int) -> str:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} updated."


@app.delete("/user/{user_id}")
async def delete_user(user_id: str) -> str:
    del users[user_id]
    return f"User {user_id} deleted."

# uvicorn module_16_3:app --reload

# tasklist | find "uvicorn"

# taskkill /PID <PID> /F