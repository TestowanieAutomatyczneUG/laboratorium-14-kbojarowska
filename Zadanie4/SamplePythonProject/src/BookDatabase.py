class BookDatabase:
    def __init__(self, books=None):
        if books is None:
            books = []
        self.books = books

    def getBookList(self):
        pass

    def getBookById(self, book_id):
        pass

    def addBook(self, book):
        pass

    def deleteBook(self, book_id):
        pass