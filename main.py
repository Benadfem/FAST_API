from fastapi import FastAPI

app = FastAPI()


# the hard coded database for the project
BOOKS = [
    {"title": "Clean Code", "author": "Robert C. Martin", "category": "Programming"},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "category": "Fantasy"},
    {"title": "Atomic Habits", "author": "James Clear", "category": "Self-Help"},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "category": "Classic"},
    {"title": "Deep Learning", "author": "Ian Goodfellow", "category": "AI & Tech"},
    {"title": "Dune", "author": "Frank Herbert", "category": "Science Fiction"},
    {"title": "The Psychology of Money", "author": "Morgan Housel", "category": "Finance"},
    {"title": "Python Crash Course", "author": "Eric Matthes", "category": "Programming"}
]

@app.get("/")
async def read_root():
    return {"Message": "Welcome to My Book app"}


@app.get("/books")
async def read_all_books():
    return BOOKS