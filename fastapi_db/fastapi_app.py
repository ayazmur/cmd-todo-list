from fastapi import FastAPI, HTTPException, Depends
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from uuid import UUID
from typing import List
from database import SessionLocal
from sql_db.models import Task
from AbstractDBManager import AbstractDBManager
from general.TaskExceptions import TaskExistingException, TaskCompletedException


app = FastAPI()

db_manager: AbstractDBManager = None
app.mount("/static", StaticFiles(directory="static"), name="static")


class TaskCreate(BaseModel):
    task_text: str


class TaskResponse(BaseModel):
    id: UUID
    task_text: str
    is_active: bool

    class Config:
        from_attributes = True


def setup_db_manager(manager: AbstractDBManager):
    """
    устанавливет менеджер базы данных
    :param manager: абстрактный менеджер базы данных
    :return:
    """
    global db_manager
    db_manager = manager


# Эндпоинты API
@app.get("/tasks/", response_model=List[TaskResponse])
def get_all_tasks():
    """Получить все задачи"""
    with SessionLocal() as session:
        tasks = session.query(Task).all()
        return tasks


@app.post("/tasks/", response_model=TaskResponse)
def create_task(task: TaskCreate):
    """Создать новую задачу"""
    try:
        new_task = db_manager.add_task(task.task_text)
        return new_task
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: UUID, task: TaskCreate):
    """Обновить задачу"""
    try:
        db_manager.edit_task(task_id, task.task_text)
        with SessionLocal() as session:
            updated_task = session.get(Task, task_id)
            return updated_task
    except TaskExistingException as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.put("/tasks/{task_id}/complete", response_model=TaskResponse)
def complete_task(task_id: UUID):
    """Завершить задачу"""
    try:
        db_manager.mark_done(task_id)
        with SessionLocal() as session:
            task = session.get(Task, task_id)
            return task
    except (TaskExistingException, TaskCompletedException) as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.delete("/tasks/{task_id}")
def delete_task(task_id: UUID):
    """Удалить задачу"""
    try:
        db_manager.delete_task(task_id)
        return {"message": "Task deleted successfully"}
    except TaskExistingException as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/")
async def read_root():
    return {"message": "Перейдите на /static/index.html"}
