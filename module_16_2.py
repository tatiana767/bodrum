
'''Задача "Аннотация и валидация":
Допишите валидацию для маршрутов из предыдущей задачи при помощи классов Path и Annotated:
'/user/{user_id}' - функция, выполняемая по этому маршруту, принимает аргумент user_id,
для которого необходимо написать следующую валидацию:
Должно быть целым числом
Ограничено по значению: больше или равно 1 и меньше либо равно 100.
Описание - 'Enter User ID'
Пример - '1' (можете подставить свой пример не противоречащий валидации)
'/user' замените на '/user/{username}/{age}' - функция, выполняемая по этому маршруту,
 принимает аргументы username и age, для которых необходимо написать следующую валидацию:
username - строка, age - целое число.
username ограничение по длине: больше или равно 5 и меньше либо равно 20.
age ограничение по значению: больше или равно 18 и меньше либо равно 120.
Описания для username и age - 'Enter username' и 'Enter age' соответственно.
Примеры для username и age - 'UrbanUser' и '24' соответственно.
(можете подставить свои примеры не противоречащие валидации).'''


from fastapi import FastAPI, Path
from typing import Annotated
app = FastAPI()

@app.get("/")
async def root():
 return {"message": "Главная страница"}

@app.get("/users/admin")
async def admin():
  return {"message": "Вы вошли как администратор"}

@app.get("/users/{user_id}")
async def read_user1(
user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID")]):
  return {"message": f"Вы вошли как durak User{user_id}"}


@app.get("/users/{username}/{age}")
async def read_name_age(
        username: Annotated[str, Path(min_length=3, max_length=20, description="Enter username")],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age")]):
  return {f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
