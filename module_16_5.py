

from fastapi import FastAPI, Request, HTTPException, Path
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from typing import Annotated, List
app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True}, debug=True)
# Настраиваем Jinja2 для загрузки шаблонов из папки templates
templates = Jinja2Templates(directory="templates")







class User(BaseModel):
    id: int
    username: str
    age: int

a = User(id = 1, username = 'Petrov', age =  25)
b = User(id= 2,username = 'Drozdov', age = 32)


users = [a, b]


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users})



@app.get("/users/{user_id}")
async def get_users(request: Request, user_id : Annotated[int, Path(ge=1)]):
    for user in users:
        if user.id == user_id :
            return templates.TemplateResponse("users.html", {"request": request, "user": user})



@app.post("/user/{username}/{age}")
async def create_user(username: str, age: int):
  new_user_id = users[-1].id +1  if users else 1
  new_user = User(id = new_user_id, username = username, age = age)
  users.append(new_user)
  return new_user



@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int, username: str, age: int):

    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user

    raise HTTPException(status_code=404, detail="User was not found")



@app.delete("/user/{user_id}")
async def delete_user(user_id: int):

    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user

    raise HTTPException(status_code=404, detail="User was not found")
