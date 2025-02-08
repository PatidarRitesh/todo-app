from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth import get_current_user
from app import schemas
from app import models
router = APIRouter()

from app.models import Todo  

@router.get("/todos/")
def get_todos(db: Session = Depends(get_db), user=Depends(get_current_user)):
    try:
        return db.query(Todo).filter(Todo.user_id == user.id).all()
    except Exception as e:
        raise HTTPException(status_code=400, detail="Error getting todos")
    

@router.post("/todos/")
def create_todo(db: Session, todo: schemas.TodoCreate, user_id: int):
    try:
        if not user_id:
            raise HTTPException(status_code=400, detail="User ID is required")

        db_todo = models.Todo(**todo.dict(), user_id=user_id)
        db.add(db_todo)
        db.commit()
        db.refresh(db_todo)
        return db_todo
    except Exception as e:
        raise HTTPException(status_code=400, detail="Error creating todo")



