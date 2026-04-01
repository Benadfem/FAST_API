"""
This is a new project for the continuation of the book project we are working on.

"""
from fastapi import FastAPI, Body


#  I want to create a new class to create the book object
class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id: int, title: str, author: str, description: str, rating: int) -> None:
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating




app = FastAPI()


# let's create a list of books
BOOKS = [
    Book(id=1, title="Read Well", author="George Best", description="A very good book", rating=5),
    Book(id=2, title="Just a life", author="Ben Thompson", description="An awesome book", rating=4),
    Book(id=3, title="Early Programmer", author="Benson Adedara", description="Teaches greatness ", rating=5),
    Book(id=4, title="give a title", author="no one", description="just a description", rating=3),
    Book(id=5, title="give a title", author="no one", description="Just a description ", rating=4),
]


@app.get("/books")
async def read_all_books():
    return BOOKS

# let's create a post request for the project
@app.post("/new_book")
async def new_book(book=Body()):
    BOOKS.append(book)
    return BOOKS