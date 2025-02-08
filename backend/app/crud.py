from sqlalchemy.orm import Session
from . import models, schemas
from fastapi import HTTPException
# def create_todo(db: Session, todo: schemas.TodoCreate):
#     db_todo = models.Todo(**todo.dict())
#     db.add(db_todo)
#     db.commit()
#     db.refresh(db_todo)
#     return db_todo

def create_todo(db: Session, todo: schemas.TodoCreate, user_id: int):  # Added user_id here
    db_todo = models.Todo(**todo.dict(), user_id=user_id)  # Assign user_id while creating the ToDo
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo
# def get_todos(db: Session):
#     return db.query(models.Todo).all()


def get_todos(db: Session, user_id: int):
    return db.query(models.Todo).filter(models.Todo.user_id == user_id).all()

def get_todo_by_id(db: Session, todo_id: int):
    return db.query(models.Todo).filter(models.Todo.id == todo_id).first()



def update_todo(db: Session, todo_id: int, todo_update: schemas.TodoUpdate):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    # Update only provided fields
    for key, value in todo_update.dict(exclude_unset=True).items():
        setattr(db_todo, key, value)

    db.commit()
    db.refresh(db_todo)
    return db_todo


def delete_todo(db: Session, todo_id: int):
    db_todo = get_todo_by_id(db, todo_id)
    if db_todo:
        db.delete(db_todo)
        db.commit()
    return db_todo