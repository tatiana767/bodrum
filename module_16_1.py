
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
 return {"message": "Главная страница"}

@app.get("/users/admin")
async def admin():
  return {"message": "Вы вошли как администратор"}

@app.get("/users/{user_id}")
async def read_user(user_id: int):
  return {"message": f"Вы вошли как User{user_id}"}


@app.get("/users/")
async def read_name_age( username : str, age: int):
  return {f"Информация о пользователе. Имя: {username}, Возраст: {age}"}