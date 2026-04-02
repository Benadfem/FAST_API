"""
This is a new project for the continuation of the book project we are working on.

"""
from dataclasses import Field, field

from fastapi import FastAPI
from pydantic import BaseModel, Field


#  I want to create a new class to create the book object
class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int

    def __init__(self, id: int, title: str, author: str, description: str, rating: int, published_date: int ) -> None:
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date

# I will create a new class for the book request inheriting the BaseModel from the pydantic
# I will implement validation for every of my data
class BookRequest(BaseModel):

    id: int | None = Field(description="ID not needed on create", default=None)
    title: str = Field(min_length= 3)
    author: str = Field(min_length=3, max_length=25)
    description: str = Field(min_length=1, max_length=30)
    rating: int = Field(gt=-1, lt=6)
    published_date: int = Field(gt=0, lt=2027)

#     we can change the default display of the value on the swagger schema
    model_config = {
        "json_schema_extra":{
            "example":{
                "title":"A default Book",
                "author":"Benson Adedara",
                "description":"This is just a sample book for the schema",
                "rating":5,
                "published_date":2002
            }
        }
    }


app = FastAPI()


# let's create a list of books
BOOKS = [
    Book(id=1, title="Read Well", author="George Best", description="A very good book", rating=5, published_date=2010),
    Book(id=2, title="Just a life", author="Ben Thompson", description="An awesome book", rating=4, published_date=2010),
    Book(id=3, title="Early Programmer", author="Benson Adedara", description="Teaches greatness ", rating=5, published_date=2015),
    Book(id=4, title="give a title", author="no one", description="just a description", rating=3, published_date=2020),
    Book(id=5, title="give a title", author="no one", description="Just a description ", rating=4, published_date=2026),
]


@app.get("/books")
async def read_all_books():
    return BOOKS

"""
we can decide to get a book by an ID
so you search for a book in the shelf with the ID
"""
@app.get("/books/{book_id}")
async def read_book_by_id(book_id: int):
    for book in BOOKS:
        if book.id == book_id:
            return book

"""
we can filter the book by rating
"""
@app.get("/books/filter/")
async def read_by_book_rating(book_rating : int):
    books_by_rating = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_by_rating.append(book)
    return books_by_rating


"""
Now we can update the book by the book id using the BookRequest from pydantic
"""
@app.put("/books/update_book")
async def update_book(book: BookRequest):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book

"""
To delete a book from the list of books 
we create an endpoint with path parameter
"""
@app.delete("/books/{book_id}")
async def delete_book_by_id(book_id: int):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            break

# let's create a post request for the project
@app.post("/new_book")
async def new_book(book: BookRequest):
    new_book = Book(**book.dict())
    BOOKS.append(book_id(new_book))

# I will create a function to increment the id for the data validation
def book_id(book: Book):
     book.id =1 if len(BOOKS) == 0 else BOOKS[-1].id +1
     return book

"""
Assignment

Here is your opportunity to keep learning!

Add a new field to Book and BookRequest called published_date: int (for example,
published_date: int = 2012). So, this book as published on the year of 2012.

Enhance each Book to now have a published_date

Then create a new GET Request method to filter by published_date
"""

# Having fix the necessary published_date everywhere,
# let's create an endpoint for it
@app.get("/books/published_date/")
async def read_all_books_published_date(date : int):
    published_book_by_date = []
    for book in BOOKS:
        if book.published_date == date:
            published_book_by_date.append(book)
    return published_book_by_date
