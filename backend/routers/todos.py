# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from app.database import get_db
# # from app.models import ToDo
# from app.auth import get_current_user
# from app import schemas
# from app import models
# router = APIRouter()

# # @router.get("/todos/")
# # def get_todos(db: Session = Depends(get_db), user=Depends(get_current_user)):
# #     return db.query(ToDo).filter(ToDo.user_id == user.id).all()
# from app.models import Todo  # Correct import

# @router.get("/todos/")
# def get_todos(db: Session = Depends(get_db), user=Depends(get_current_user)):
#     return db.query(Todo).filter(Todo.user_id == user.id).all()
# # @router.post("/todos/")
# # def create_todo(title: str, description: str, due_date: str, db: Session = Depends(get_db), user=Depends(get_current_user)):
# #     new_todo = ToDo(title=title, description=description, due_date=due_date, user_id=user.id)
# #     db.add(new_todo)
# #     db.commit()
# #     return new_todo
# @router.post("/todos/")
# def create_todo(db: Session, todo: schemas.TodoCreate, user_id: int):
#     if not user_id:
#         raise HTTPException(status_code=400, detail="User ID is required")

#     # Correctly assigning user_id to the ToDo
#     db_todo = models.ToDo(**todo.dict(), user_id=user_id)
#     db.add(db_todo)
#     db.commit()
#     db.refresh(db_todo)
#     return db_todo






from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
# from app.models import ToDo
from app.auth import get_current_user
from app import schemas
from app import models
router = APIRouter()

# @router.get("/todos/")
# def get_todos(db: Session = Depends(get_db), user=Depends(get_current_user)):
#     return db.query(ToDo).filter(ToDo.user_id == user.id).all()
from app.models import Todo  # Correct import

@router.get("/todos/")
def get_todos(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return db.query(Todo).filter(Todo.user_id == user.id).all()
# @router.post("/todos/")
# def create_todo(title: str, description: str, due_date: str, db: Session = Depends(get_db), user=Depends(get_current_user)):
#     new_todo = ToDo(title=title, description=description, due_date=due_date, user_id=user.id)
#     db.add(new_todo)
#     db.commit()
#     return new_todo
@router.post("/todos/")
def create_todo(db: Session, todo: schemas.TodoCreate, user_id: int):
    if not user_id:
        raise HTTPException(status_code=400, detail="User ID is required")

    # Correctly assigning user_id to the ToDo
    db_todo = models.Todo(**todo.dict(), user_id=user_id)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo



