"""
This is a new project for the continuation of the book project we are working on.

"""
from dataclasses import Field

from fastapi import FastAPI
from pydantic import BaseModel, Field


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

# I will create a new class for the book request inheriting the BaseModel from the pydantic
# I will implement validation for every of my data
class BookRequest(BaseModel):

    id: int | None = Field(description="ID not needed on create", default=None)
    title: str = Field(min_length= 3)
    author: str = Field(min_length=3, max_length=25)
    description: str = Field(min_length=1, max_length=30)
    rating: int = Field(gt=-1, lt=6)

#     we can change the default display of the value on the swagger schema
    model_config = {
        "json_schema_extra":{
            "example":{
                "title":"A default Book",
                "author":"Benson Adedara",
                "description":"This is just a sample book for the schema",
                "rating":5
            }
        }
    }


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

"""
we can decide to get a book by an ID
so you search for a book in the shelf with the ID
"""
@app.get("/books/{book_id}")
async def get_book(book_id: int):
    for book in BOOKS:
        if book.id == book_id:
            return book

# let's create a post request for the project
@app.post("/new_book")
async def new_book(book: BookRequest):
    new_book = Book(**book.dict())
    BOOKS.append(book_id(new_book))

# I will create a function to increment the id for the data validation
def book_id(book: Book):
     book.id =1 if len(BOOKS) == 0 else BOOKS[-1].id +1
     return book
