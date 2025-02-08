# from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
# from .database import Base

# class Todo(Base):
#     __tablename__ = "todos"
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, nullable=False)
#     description = Column(String, nullable=True)
#     due_date = Column(Date, nullable=True)
#     status = Column(String, default="Pending")



# from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.orm import relationship
# from .database import Base

# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String, unique=True, index=True)
#     email = Column(String, unique=True, index=True)
#     hashed_password = Column(String)

#     todos = relationship("ToDo", back_populates="owner")

# class ToDo(Base):
#     __tablename__ = "todos"

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     description = Column(String, nullable=True)
#     due_date = Column(String, nullable=True)
#     status = Column(String, default="Pending")
#     user_id = Column(Integer, ForeignKey("users.id"))

#     owner = relationship("User", back_populates="todos")





# from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.orm import relationship
# from .database import Base

# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String, unique=True, index=True)
#     email = Column(String, unique=True, index=True)
#     hashed_password = Column(String)

#     todos = relationship("Todo", back_populates="owner")  # Fix case here

# # class Todo(Base):  # Changed from ToDo → Todo
# #     __tablename__ = "todos"

# #     id = Column(Integer, primary_key=True, index=True)
# #     title = Column(String, index=True)
# #     description = Column(String, nullable=True)
# #     due_date = Column(String, nullable=True)
# #     status = Column(String, default="Pending")
# #     user_id = Column(Integer, ForeignKey("users.id"))

# #     owner = relationship("User", back_populates="todos")
# class Todo(Base):
#     __tablename__ = "todos"

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     description = Column(String, nullable=True)
#     due_date = Column(String, nullable=True)
#     status = Column(String, default="Pending")
#     user_id = Column(Integer, ForeignKey("users.id"), nullable=False)  # Ensure ForeignKey
#     owner = relationship("User", back_populates="todos")





from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    # todos = relationship("Todo", back_populates="owner") 
    todos = relationship("Todo", back_populates="owner", cascade="all, delete-orphan")

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, nullable=True)
    due_date = Column(String, nullable=True)
    status = Column(String, default="Pending")
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)  # Ensure ForeignKey
    owner = relationship("User", back_populates="todos")
