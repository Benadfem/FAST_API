from fastapi import Body, FastAPI

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


"""
new information can be added to you database
in this case new book can be added to the database BOOKS

FastAPI has a module called body we have to import it 
"""

@app.post("/new_books/")
async def create_new_book(new_book = Body()):
    BOOKS.append(new_book)
    return BOOKS

"""
We can update our database data with the put method from FastAPI

this put method also uses the Body module.
"""
@app.put("/books/updated_book")
async def update_book(updated_book= Body()):
    book_updated = False
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == updated_book.get("title").casefold():
            BOOKS[i].update(updated_book)
            break
    if book_updated:
        return BOOKS
    else:
        return {"Error": f"Book with title '{updated_book.get('title')}' not found."}
