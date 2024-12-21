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
async def post_user(username: str, age: int):
    user_id = users[-1].id + 1 if users else 1
    users.append(user := User(id=user_id, username=username, age=age))
    return user



@app.put("/user/{user_id}/{username}/{age}")
async def put_user(user_id: int, username: str, age: int):
    for i, user in enumerate(users):
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
async def delete_user(user_id: int):
    for i, user in enumerate(users):
        if user.id == user_id:
            users.pop(i)
            return user
    raise HTTPException(status_code=404, detail="User was not found")
