from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine, Base
from fastapi.middleware.cors import CORSMiddleware
Base.metadata.create_all(bind=engine)

from routers import users  # Import the 'users' router for authentication routes


app = FastAPI()

# Include the user authentication routes in your FastAPI app
app.include_router(users.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (for development)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# @app.post("/todos/", response_model=schemas.TodoResponse)
# def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
#     return crud.create_todo(db, todo)
from .auth import get_current_user  # Import get_current_user

# @app.post("/todos/", response_model=schemas.TodoResponse)
# def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
#     return crud.create_todo(db, todo, user_id=user.id)

# @app.get("/todos/", response_model=list[schemas.TodoResponse])
# def read_todos(db: Session = Depends(get_db)):
#     return crud.get_todos(db)

# @app.get("/todos/{todo_id}", response_model=schemas.TodoResponse)
# def read_todo(todo_id: int, db: Session = Depends(get_db)):
#     db_todo = crud.get_todo_by_id(db, todo_id)
#     if db_todo is None:
#         raise HTTPException(status_code=404, detail="Todo not found")
#     return db_todo

# @app.put("/todos/{todo_id}", response_model=schemas.TodoResponse)
# def update_todo(todo_id: int, todo: schemas.TodoUpdate, db: Session = Depends(get_db)):
#     return crud.update_todo(db, todo_id, todo)

# @app.delete("/todos/{todo_id}")
# def delete_todo(todo_id: int, db: Session = Depends(get_db)):
#     db_todo = crud.delete_todo(db, todo_id)
#     if db_todo is None:
#         raise HTTPException(status_code=404, detail="Todo not found")
#     return {"message": "Todo deleted successfully"}
@app.post("/todos/", response_model=schemas.TodoResponse)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return crud.create_todo(db, todo, user_id=user.id)

@app.get("/todos/", response_model=list[schemas.TodoResponse])
def read_todos(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return crud.get_todos(db, user_id=user.id)

@app.get("/todos/{todo_id}", response_model=schemas.TodoResponse)
def read_todo(todo_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    db_todo = crud.get_todo_by_id(db, todo_id)
    if db_todo is None or db_todo.user_id != user.id:
        raise HTTPException(status_code=404, detail="Todo not found or unauthorized")
    return db_todo

@app.put("/todos/{todo_id}", response_model=schemas.TodoResponse)
def update_todo(todo_id: int, todo: schemas.TodoUpdate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    db_todo = crud.get_todo_by_id(db, todo_id)
    if db_todo is None or db_todo.user_id != user.id:
        raise HTTPException(status_code=404, detail="Todo not found or unauthorized")
    return crud.update_todo(db, todo_id, todo)

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    db_todo = crud.get_todo_by_id(db, todo_id)
    if db_todo is None or db_todo.user_id != user.id:
        raise HTTPException(status_code=404, detail="Todo not found or unauthorized")
    return crud.delete_todo(db, todo_id)
