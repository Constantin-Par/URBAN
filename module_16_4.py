from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    age: int


app = FastAPI()
users = []


@app.get("/users")
async def get_users() -> list:
    return users


@app.post("/user/{username}/{age}")
async def post_user(username: str, age: int) -> str:
    user = User(id=len(users) + 1, username=username, age=age)
    users.append(user)
    return f"User {user.id} {user.username} registered."

# @app.post("/user/")
# async def post_user(user: User) -> str:
#     user.id = len(users) + 1
#     users.append(user)
#     return f"User {user.id} {user.username} registered."


@app.put("/user/{user_id}/{username}/{age}")
async def put_user(user_id: int, username: str, age: int) -> str:
    try:
        user = users[user_id - 1]
        username_old = user.username
        age_old = user.age
        user.username = username
        user.age = age
        return f"User {user_id - 1} updated: {username_old}->{username} {age_old}->{age}"
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
async def delete_user(user_id: int) -> str:
    try:
        user = users.pop(user_id - 1)
        username = user.username
        return f"User {user_id - 1} {username} deleted."
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")

# uvicorn module_16_4:app --reload
# http://127.0.0.1:8000/docs
# tasklist | find "uvicorn"
# taskkill /PID <PID> /F
