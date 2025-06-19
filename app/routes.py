from fastapi import APIRouter
from app.models import Task

router = APIRouter()

fake_tasks = []

@router.post("/tasks")
def create_task(task: Task):
	fake_tasks.append(task)
	return {"message": "Task added", "task": Task}

@router.get("/tasks")
def get_tasks():
	return fake_tasks

