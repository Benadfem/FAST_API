
"""
this hold the database for the project
"""

from .models import Book

# let's create a list of books
BOOKS = [
    Book(id=1, title="Read Well", author="George Best", description="A very good book", rating=5),
    Book(id=2, title="Just a life", author="Ben Thompson", description="An awesome book", rating=4),
    Book(id=3, title="Early Programmer", author="Benson Adedara", description="Teaches greatness ", rating=5),
    Book(id=4, title="give a title", author="no one", description="just a description", rating=3),
    Book(id=5, title="give a title", author="no one", description="Just a description ", rating=4),
]
