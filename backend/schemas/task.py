from typing import Optional
from pydantic import BaseModel, ConfigDict
from schemas.users import User
from datetime import datetime

class TaskStatus(BaseModel):
    model_config= ConfigDict(from_attributes=True)
    id: Optional[int] = None
    name: str
    description: Optional[str]
    color: str = "#FFFFFF"  
    created_at: Optional[datetime]= None
    updated_at: Optional[datetime]= None

class Task(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: Optional[int] = None
    title: str
    description: Optional[str]
    assigned_user: User
    status: TaskStatus
    due_date: Optional[datetime] = None
    created_at: Optional[datetime]= None
    updated_at: Optional[datetime]= None

class CreateTask(BaseModel):
    title: str
    description: Optional[str] = None
    status:Optional[str] =None
    due_date:Optional[datetime] = None


