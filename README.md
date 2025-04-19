Thanks for the clarification! Here's your **final cleaned-up and professional `README.md`**, formatted exactly as you described — no leftover triggers, with a full DevOps-ready structure including optional sections for Docker and CI/CD.

---

```markdown
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
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the App Locally
```bash
uvicorn app.main:app --reload
```

Then visit: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🐳 Docker Support

You can run the app using Docker:

```bash
# Build the image
docker build -t quote-api .

# Run the container
docker run -d -p 8000:8000 quote-api
```

Then visit: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🔐 CI/CD & Security

- ✅ CI triggered on `main`, `dev`, and `staging` branches  
- ✅ Linting using `flake8`  
- ✅ Unit testing using `pytest`  
- ✅ CodeQL security scanning  
- ✅ Pytest logs uploaded as GitHub Actions artifacts  
- ✅ Branch protection enabled on `main`

---
```

✅ Copy-paste this into your `README.md` to finalize.  
Let me know when it's committed or if you want help pushing it to `main`, `dev`, and `staging`.
