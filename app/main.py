from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from app.database import create_table
from pydantic import BaseModel
from app.database import add_task
from app.database import get_all_tasks
from app.database import delete_task
from app.database import update_task

app = FastAPI()


templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"title": "Task Manager"}

)
class TaskCreate(BaseModel):
    title: str


@app.post("/tasks")
def create_task(task: TaskCreate):
    add_task(task.title)

    return {
        "message": "Task created successfully!",
        "task": task.title
    }
@app.get("/tasks")
def read_tasks():
    tasks = get_all_tasks()

    return {"tasks": [dict(task) for task in tasks]}

@app.delete("/tasks/{task_id}")
def remove_task(task_id: int):
    delete_task(task_id)

    return {"message": "Task deleted successfully!"}

class TaskUpdate(BaseModel):
    title: str
    completed: int


@app.put("/tasks/{task_id}")
def edit_task(task_id: int, task: TaskUpdate):
    update_task(task_id, task.title, task.completed)

    return {
        "message": "Task updated successfully!"
    }