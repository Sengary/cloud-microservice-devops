# Quote Manager API

A cloud-based microservice built with FastAPI, deployed via Render, and maintained using GitHub Actions CI/CD.

## 👥 Team Members

- **Mohab Hussien** (CI/CD Engineer)  
- **Abdulrahman Sharqawi** (Developer)  
- **Basil Al-Ashqar** (Operations/QA)


## 🔧 Features
- GET and POST inspirational quotes
- Health check endpoint
- Swagger API documentation at `/docs`

## 🚀 Live URL
https://quote-api-hucb.onrender.com

## 📦 Tech Stack
- FastAPI
- Uvicorn
- GitHub Actions (CI)
- Render (Cloud Hosting)
- Pytest (Unit Testing)

## ⚙️ Setup (Locally)
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
