# 📚 FastAPI Book Management API

A lightweight REST API built with Python and FastAPI to manage a collection of books.

## 🚀 Features
- **Get All Books**: Retrieve the full list of books in the database.
- **Search by Title**: Use path parameters to find specific books (case-insensitive).
- **Auto-Documentation**: Interactive Swagger UI generated automatically.

## 🛠️ Tech Stack
- **Language**: Python
- **Framework**: FastAPI
- **Web Server**: Uvicorn
- **Version Control**: Git & GitHub

## 📖 How to Run Locally
1. Clone the repo: `git clone https://github.com/Benadfem/FAST_API.git`
2. Create venv: `python -m venv venv`
3. Install dependencies: `pip install -r requirements.txt`
4. Run server: `uvicorn main:app --reload`
5. Visit: `http://127.0.0.1:8000/docs`