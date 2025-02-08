# todo-app

### This is a simple todo app backend built using Python FastAPI and PostgreSQL. and frontend built using Html, css , javascript.

## Features
- Signup
- Login
- Logout
- Create todo
- Update todo
- Delete todo
- Get all todos
  
## Installation
- Clone the repository
- Install the dependencies using `pip install -r requirements.txt`
- Create a `.env` file and add the following environment variables
  - `DATABASE_URL` : PostgreSQL database url
  - `SECRET_KEY` : Secret key for encoding and decoding jwt tokens
  - `ALGORITHM` : Algorithm used for encoding and decoding jwt tokens

## Run the backend app using `uvicorn main:app --reload`
## Run the frontend app using `python -m http.server 8001`
## Open the browser and go to `http://localhost:8001`

## API Documentation
- Go to `http://localhost:8000/docs` to view the API documentation after running the backend app
- Go to `http://localhost:8000/redoc` to view the API documentation after running the backend app

