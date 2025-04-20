from sqlalchemy import Column, Table, ForeignKey
from sqlalchemy import Integer, String, DateTime
from typing import List, Optional
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from config.db import meta, engine, Base

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from task import TaskTable



class UserTable(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    username: Mapped[str] = mapped_column(String(50),index=True, unique=True)
    email: Mapped[str] = mapped_column(String(100),index=True, unique=True)
    password: Mapped[str] = mapped_column(String(100))
    tasks: Mapped[list["TaskTable"]] = relationship("TaskTable", back_populates="assigned_user")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)



