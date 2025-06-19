from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base


class Task(BaseModel):
	title: str
	description: str | None = None
	completed: bool = False

class TaskDB(Base):
	__tablename__ = "tasks"

	id = Column(Integer, primary_key=True, index=True)
	title = Column(String, index=True)
	description = Column(String, nullable=True)
	completed = Column(Boolean, default=False)

class TaskResponse(Task):
	id: int

	class Config:
		orm_mode = True
