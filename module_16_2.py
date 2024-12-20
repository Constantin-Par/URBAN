from typing import Annotated
from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Главная страница"}


@app.get("/user/admin")
async def user_admin() -> str:
    return "Вы вошли как администратор"


@app.get("/user/{used_id}")
async def get_user_id(used_id: Annotated[int, Path(ge=1, le=100,
                                                   description="Enter User ID from 1 to 100",
                                                   example="2")]) -> str:
    return f"Вы вошли как пользователь № {used_id}"


@app.get("/user/{username}/{age}")
async def get_user_age(username: Annotated[str, Path(min_length=5, max_length=20,
                                                     description="Enter username, lenght from 5 to 20",
                                                     example="UrbanUser")],
                       age: Annotated[int, Path(ge=18, le=120,
                                                description="Enter age from 18 to 120",
                                                example="24")]) -> str:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"

# python -m uvicorn module_16_2:app --reload
# uvicorn module_16_2:app --reload
# tasklist | find "uvicorn"
# taskkill /PID <PID> /F