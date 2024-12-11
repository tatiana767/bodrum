''''В файле main.py создайте сущность FastAPI(), напишите один маршрут для неё - '/', по которому функция
возвращает словарь - {"message": "Welcome to Taskmanager"}.'''



from fastapi import FastAPI
from route import task, user

app = FastAPI()

app.include_router(task.router)
app.include_router(user.router)
@app.get("/")
async def welcome():
  return {"message": "Welcome to Taskmanager"}