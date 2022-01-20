from src.Author import Author
from src.validateISBNNumber import validateISBNNumber


class Book:
    def __init__(self, title, author, isbn):
        if type(title) is not str or title == "":
            raise Exception("Bad title ")
        elif not isinstance(author, Author):
            raise Exception("Author must be an author")
        elif not validateISBNNumber.validate(isbn):
            raise Exception("Bad isbn number")
        self.title = title
        self.author = author
        self.isbn = isbn
