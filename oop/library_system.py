class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author    

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size:int):
        super().__init__(title, author)
        self.file_size = file_size


class PrintBook(Book):
    def __init__(self, title, author, page_count:int):
        super().__init__(title, author)
        self.page_count = page_count


class Library:
    def __init__(self, book:list=None):
        self.book = book or []  # avoid mutable default

    def add_book(self, book):
        self.book.append(book)

    def list_books(self):
        for book in self.book:
            if isinstance(book, EBook):
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            elif isinstance(book, Book):
                print(str(book))
