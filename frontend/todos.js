const API_BASE_URL = "http://127.0.0.1:8000";
let editingTodoId = null; // Store the ID of the todo being edited

// Signup
if (document.getElementById("signupForm")) {
    document.getElementById("signupForm").addEventListener("submit", async (e) => {
        e.preventDefault();
        const username = document.getElementById("signupUsername").value;
        const email = document.getElementById("signupEmail").value;
        const password = document.getElementById("signupPassword").value;

        const response = await fetch(`${API_BASE_URL}/signup/`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username, email, password }),
        });

        if (response.ok) {
            alert("Signup successful! Please log in.");
            window.location.href = "index.html";
        } else {
            alert("Signup failed.");
        }
    });
}

// Login
if (document.getElementById("loginForm")) {
    document.getElementById("loginForm").addEventListener("submit", async (e) => {
        e.preventDefault();
        const username = document.getElementById("loginUsername").value;
        const password = document.getElementById("loginPassword").value;

        const formData = new URLSearchParams();
        formData.append("username", username);
        formData.append("password", password);

        const response = await fetch(`${API_BASE_URL}/login/`, {
            method: "POST",
            headers: { "Content-Type": "application/x-www-form-urlencoded" },
            body: formData,
        });

        if (response.ok) {
            const data = await response.json();
            localStorage.setItem("token", data.access_token);
            window.location.href = "dashboard.html";
        } else {
            alert("Login failed.");
        }
    });
}

// Fetch To-Dos
async function fetchTodos() {
    const token = localStorage.getItem("token");
    const response = await fetch(`${API_BASE_URL}/todos/`, {
        headers: { Authorization: `Bearer ${token}` },
    });

    if (!response.ok) {
        alert("Failed to fetch todos.");
        return;
    }

    const todos = await response.json();
    const todoList = document.getElementById("todoList");
    todoList.innerHTML = "";

    todos.forEach((todo) => {
        const li = document.createElement("li");
        li.innerHTML = `
            <strong>${todo.title}</strong> - ${todo.description} - Due: ${todo.due_date} - Status: ${todo.status}
            <button onclick="editTodo(${todo.id})">Edit</button>
            <button onclick="deleteTodo(${todo.id})">Delete</button>
            <button onclick="markCompleted(${todo.id})">Mark Completed</button>
        `;
        todoList.appendChild(li);
    });
}

// Add/Edit To-Do
if (document.getElementById("todoForm")) {
    document.getElementById("todoForm").addEventListener("submit", async (e) => {
        e.preventDefault();
        const token = localStorage.getItem("token");
        const title = document.getElementById("todoTitle").value;
        const description = document.getElementById("todoDescription").value;
        const due_date = document.getElementById("todoDueDate").value;
        const status = document.getElementById("todoStatus").value;
        
        const payload = { title, description, due_date, status };

        if (editingTodoId) {
            // Edit existing todo
            await fetch(`${API_BASE_URL}/todos/${editingTodoId}`, {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json",
                    Authorization: `Bearer ${token}`,
                },
                body: JSON.stringify(payload),
            });
            editingTodoId = null; // Reset editing ID
        } else {
            // Add new todo
            await fetch(`${API_BASE_URL}/todos/`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    Authorization: `Bearer ${token}`,
                },
                body: JSON.stringify(payload),
            });
        }

        document.getElementById("todoForm").reset();
        fetchTodos();
    });
}

// Delete To-Do
async function deleteTodo(id) {
    const token = localStorage.getItem("token");
    await fetch(`${API_BASE_URL}/todos/${id}`, {
        method: "DELETE",
        headers: { Authorization: `Bearer ${token}` },
    });
    fetchTodos();
}

// Mark Completed
async function markCompleted(id) {
    const token = localStorage.getItem("token");
    await fetch(`${API_BASE_URL}/todos/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json", Authorization: `Bearer ${token}` },
        body: JSON.stringify({ status: "Completed" }),
    });
    fetchTodos();
}

// Edit To-Do
function editTodo(id) {
    const token = localStorage.getItem("token");
    fetch(`${API_BASE_URL}/todos/${id}`, {
        headers: { Authorization: `Bearer ${token}` },
    })
    .then(response => response.json())
    .then(todo => {
        document.getElementById("todoTitle").value = todo.title;
        document.getElementById("todoDescription").value = todo.description;
        document.getElementById("todoDueDate").value = todo.due_date;
        document.getElementById("todoStatus").value = todo.status;
        editingTodoId = id;
    })
    .catch(error => console.error("Error fetching todo:", error));
}

// Logout
function logout() {
    localStorage.removeItem("token");
    window.location.href = "index.html";
}

// Load To-Dos on Page Load
if (document.getElementById("todoList")) {
    fetchTodos();
}
