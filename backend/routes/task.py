from fastapi import APIRouter, status, Depends,HTTPException
from datetime import datetime, timezone
from sqlalchemy.orm import Session
from typing import List

from config.db import get_db
from schemas.task import Task, TaskStatus, CreateTask
from schemas.users import User
from utils.auth import get_current_user
from models.task import TaskTable, TaskStatusTable


task = APIRouter(tags=["task"])


def get_new_status(status, db):
    return db.query(TaskStatusTable).filter(TaskStatusTable.name == status).first()


@task.get("/todos", response_model=List[Task])
def get_todos(user: User = Depends(get_current_user), db:Session = Depends(get_db)):
    task = db.query(TaskTable).join(TaskTable.assigned_user).filter_by(id=user.id).all()
    return task

@task.post("/todos", response_model=Task)
def create_task(task:CreateTask,user: User = Depends(get_current_user), db:Session = Depends(get_db)):
    exist = db.query(TaskTable).filter(TaskTable.name == task.name).first()
    if not exist:
        new_task = task.model_dump()
        new_task.update({"create_at":datetime.now(timezone.utc), "assigned_user": user,"status":get_new_status(task.status, db)})
        new_task = TaskTable(**new_task)
        db.add(new_task)
        db.commit()
        db.refresh(new_task)
        return new_task
    raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"task with name already exist")

