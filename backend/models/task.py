from sqlalchemy import Column, Table, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from typing import List, Optional
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.users import UserTable
    
from config.db import meta, engine, Base



class TaskStatusTable(Base):
    __tablename__ = "task_status"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    name: Mapped[str] = mapped_column(String(60),unique=True, index=True)
    description: Mapped[Optional[str]] = mapped_column(nullable=True)    
    color:  Mapped[Optional[str]] = mapped_column(nullable=True)  
    task: Mapped[Optional[List["TaskTable"]]] = relationship(back_populates="status")
    create_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    update_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True) 


class TaskTable(Base):
    __tablename__ = "task"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    name: Mapped[str] = mapped_column(String(60),unique=True, index=True)
    description: Mapped[str]
    assigned_to: Mapped[int] = mapped_column(ForeignKey("users.id"))
    assigned_user: Mapped["UserTable"] = relationship("UserTable", back_populates="tasks")
    status_id: Mapped[Optional[int]] = mapped_column(ForeignKey("task_status.id"), nullable=True)
    status: Mapped[Optional["TaskStatusTable"]] = relationship(back_populates="task")
    due_date: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    create_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    update_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)

    