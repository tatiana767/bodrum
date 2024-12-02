
'''Создайте новое приложение FastAPI и сделайте CRUD запросы.
Создайте словарь users = {'1': 'Имя: Example, возраст: 18'}
Реализуйте 4 CRUD запроса:
get запрос по маршруту '/users', который возвращает словарь users.
post запрос по маршруту '/user/{username}/{age}', который добавляет в словарь по максимальному по
значению ключом значение строки "Имя: {username}, возраст: {age}".
 И возвращает строку "User <user_id> is registered".
put запрос по маршруту '/user/{user_id}/{username}/{age}', который обновляет значение из словаря users
под ключом user_id на строку "Имя: {username}, возраст: {age}". И возвращает строку "The user <user_id> is updated"
delete запрос по маршруту '/user/{user_id}', который удаляет из словаря users по ключу user_id пару'''


from fastapi import FastAPI, Path
from typing import Annotated
app = FastAPI()


users = {'1': 'Имя: Example, возраст: 18'}






@app.get("/")
async def root():
 return {"message": "Главная "}


@app.post("/user/{username}/{age}")
async def create_user(username: str, age: int):
  new_user = int(max(users.keys())) + 1
  users[str(new_user)] = f"Имя:{username}, возраст:{age}"


  return {"message":f"User {new_user} is registered"}

@app.get("/users")
async def get_users()  -> dict() :
  return users


@app.put("/users/{user_id}/{user_name}/{age}")
async def update_users(user_id: int, user_name: str, age: int ):
  if users[str(user_id)] :

      users.update({f"{str(user_id)}": f"Имя: {user_name}, возраст:{age}"})
  return {'message' : f'The user {user_id} is updated'}


@app.delete("/users/{user_id}")
async def delete_users(user_id: int):
    if users[str(user_id)]:
       del users[str(user_id)]
    return {'message': f'The user {user_id} is deleted'}