class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author    

    def __str__(self):
        return f"{self.title}, by {self.author}"


class EBook(Book):
    def __init__(self, title, author, page_count:int, file_size:float):
        super().__init__(title, author)
        self.page_count = page_count
        self.file_size   = file_size

class PrintBook(Book):
    def __init__(self, title, author, page_count:int):
        super().__init__(title, author)
        self.page_count = page_count


class Library:
    def __init__(self, book:list=None):
        self.book = book or []  # avoid mutable default arg

    def add_book(self, book):
        self.book.append(book)

    def list_books(self):
        for book in self.book:
            if isinstance(book, (EBook, PrintBook)):   # subclasses with page_count
                print(f"{book.__class__.__name__}: {book.title}, by {book.author}, Page Count: {book.page_count}")
            elif isinstance(book, Book):  # base class
                print(f"{book.__class__.__name__}: {book.title}, by {book.author}")

