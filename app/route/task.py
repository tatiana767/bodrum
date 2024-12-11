
from fastapi import APIRouter


router = APIRouter(prefix = "/task", tags = ["task"])

@router.get("/")
async def all_tasks():
    pass

@router.get("/userd_id")
async def user_by_id():
    pass


@router.post("/create")
async def create_task():
    pass


@router.put("/update")
async def update_task():
    pass

@router.delete ("/delete")
async def delete_user():
    pass
