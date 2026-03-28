from fastapi import FastAPI

app = FastAPI()


# the hard coded database for the project
BOOKS = [
    {"title": "Clean Code", "author": "Robert C. Martin", "category": "Programming"},
    {"title": "The Hobbit", "author": "James Clear", "category": "fantasy"},
    {"title": "Atomic Habits", "author": "James Clear", "category": "fantasy"},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "category": "Classic"},
    {"title": "Deep Learning", "author": "Ian Goodfellow", "category": "AI & Tech"},
    {"title": "Dune", "author": "Frank Herbert", "category": "Science Fiction"},
    {"title": "The Psychology of Money", "author": "Morgan Housel", "category": "fantasy"},
    {"title": "Python Crash Course", "author": "Eric Matthes", "category": "Programming"}
]

@app.get("/")
async def read_root():
    return {"Message": "Welcome to My Book app"}


@app.get("/books")
async def read_all_books():
    return BOOKS

"""
let's request for specific book
from the database of books that are in the shelf

we use path parameter to fix this
"""

@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get("title").casefold() == book_title.casefold():
            return book
    return {"Error": "Book not found"}

"""

you can perform search on the database based on some argument
1. you can request a single information just as the previous code above 
2. you can search for a list of information based on similarity in the database
"""
@app.get("/books/") #this is to tell the database you want to search by list
async def search_book(searched: str):
    search_term = []
    for book in BOOKS:
        if book.get("category").casefold() == searched.casefold():
            search_term.append(book)
    return search_term

"""
we can as well add two conditions for our search 
"""
@app.get("/books/{author}/")
async def search_book_with_others(author: str, category: str):
    searched = [] #this can return more than one detail if possible
    for book in BOOKS:
        if book.get("author").casefold() == author.casefold() and \
                book.get("category").casefold() == category.casefold():#adding \ makes the line of code continued without breaking or
            searched.append(book)
    return searched

