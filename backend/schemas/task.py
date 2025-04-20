from typing import Optional
from pydantic import BaseModel, ConfigDict
from users import User

class TaskStatus(BaseModel):
    model_config= ConfigDict(from_attributes=True)
    id: Optional[int]
    name: str
    description: Optional[str]
    color: str = "#FFFFFF"  # Default color is white
    created_at: str
    updated_at: str

class Task(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: Optional[int]
    name: str
    description: Optional[str]
    assigned_to: User
    status_id: TaskStatus
    due_date: str
    created_at: str
    updated_at: str


