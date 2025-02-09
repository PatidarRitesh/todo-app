# To-Do App

This is a simple To-Do app with a **FastAPI** backend and a **HTML, CSS, JavaScript** frontend. The backend uses **PostgreSQL** for data storage and **JWT (JSON Web Tokens)** for authentication.

## 🚀 Features
- ✅ User Signup 
- 🔐 User Login & Logout (with JWT Authentication)
- 📝 Create To-Do
- ✏️ Update To-Do
- ❌ Delete To-Do
- 📋 Get All To-Dos

---

## ⚙️ Installation

1. **Clone the Repository:**  
```bash

git clone https://github.com/PatidarRitesh/todo-app.git
cd todo-app

```

2. **Install Dependencies:**  
```bash

cd todo-app/backend
pip install -r requirements.txt

```

3. **Set Up PostgreSQL Database:**  
- **Download PostgreSQL** from the [official website](https://www.postgresql.org/download/) based on your OS.
- After installation, create the database and user with the following commands:

```sql
CREATE DATABASE tododb;
CREATE USER todo_user WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE tododb TO todo_user;
GRANT ALL PRIVILEGES ON SCHEMA public TO todo_user;
```

4. **Set Up Environment Variables:**  
Create a `.env` file in the project root:
```env
DATABASE_URL=postgresql://todo_user:password@localhost/tododb
SECRET_KEY=your_secret_key
ALGORITHM=HS256  # or your preferred JWT algorithm
```

---

## 🚀 Running the App

### 📡 **Backend:**  
```bash

cd todo-app/backend/app
uvicorn main:app --reload

```

### 🌐 **Frontend:**  
```bash
python -m http.server 8001
```

### 🔗 **Access the App:**  
Open your browser and go to: [http://localhost:8001](http://localhost:8001)

---

## 📚 API Documentation
- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

