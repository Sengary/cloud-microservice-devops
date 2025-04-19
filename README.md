# 📝 Quote Manager API

A cloud-based microservice built with **FastAPI**, deployed via **Render**, and maintained using a **GitHub Actions CI/CD pipeline**. This service allows users to create, read, update, and delete inspirational quotes. All endpoints are tested with `pytest`, and the API is publicly documented with Swagger.

---

## 👥 Team Members

- **Mohab Hussien** (CI/CD Engineer)  
- **Abdulrahman Sharqawi** (Developer)  
- **Basil Al-Ashqar** (Operations/QA)

---

## 🔧 Features

- Full RESTful API: Create, Read, Update, Delete quotes
- In-memory database with auto-incrementing IDs
- `/health` endpoint for monitoring & CI deployment checks
- Auto-generated API docs via FastAPI’s Swagger at `/docs`
- Fully tested with CI automation using GitHub Actions
- Automatically deployed to Render on each push to `main`

---

## 📖 API Endpoints

| Method | Endpoint           | Description                     |
|--------|--------------------|---------------------------------|
| GET    | `/`                | Root welcome message            |
| GET    | `/health`          | Health check for CI monitoring |
| GET    | `/quotes`          | Retrieve all quotes             |
| POST   | `/quotes`          | Add a new quote                 |
| GET    | `/quotes/{id}`     | Get a quote by ID               |
| PUT    | `/quotes/{id}`     | Update a quote by ID            |
| DELETE | `/quotes/{id}`     | Delete a quote by ID            |

---

## 🚀 Live Deployment

✅ Access the live app here:  
🔗 [https://quote-api-hucb.onrender.com](https://quote-api-hucb.onrender.com)

Use `/docs` for testing all endpoints through Swagger UI.

---

## 📦 Tech Stack

- 🐍 Python + FastAPI
- 🚀 Uvicorn (ASGI server)
- 🧪 Pytest for testing
- 🔁 GitHub Actions for CI
- ☁️ Render.com for cloud deployment

---

## ⚙️ Local Setup Instructions

### 1. Clone the Repo
```bash
git clone https://github.com/Sengary/cloud-microservice-devops.git
cd cloud-microservice-devops
# trigger
# trigger
# re-run test artifact
# trigger dev branch CI
# trigger CI from dev branch
# trigger dev branch CI
# retry CI trigger
