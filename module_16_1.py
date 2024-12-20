from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Главная страница"}


@app.get("/user/admin")
async def user_admin() -> str:
    return "Вы вошли как администратор"


@app.get("/user")
async def user_age(username: str, age: int) -> str:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"


@app.get("/user/{used_id}")
async def user_id(used_id: int) -> str:
    return f"Вы вошли как пользователь № {used_id}"

# python -m uvicorn module_16_1:app --reload
