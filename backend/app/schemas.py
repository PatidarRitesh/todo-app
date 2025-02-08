from pydantic import BaseModel
from typing import Optional
from datetime import date

class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: Optional[date] = None
    status: Optional[str] = "Pending"

class TodoCreate(TodoBase):
    pass



class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    due_date: Optional[date] = None
    status: Optional[str] = None


class TodoResponse(TodoBase):
    id: int

    class Config:
        from_attributes = True
