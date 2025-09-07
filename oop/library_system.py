class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author    

    def __str__(self):
        return f"{self.title}, by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size:float):
        super().__init__(title, author)
        self.file_size = file_size

class PrintBook(Book):
    def __init__(self, title, author, page_count:int):
        super().__init__(title, author)
        self.page_count = page_count


class Library:
    def __init__(self, books:list=None):
        self.books = [] # avoid mutable default arg

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            if isinstance(book, PrintBook):   # subclasses with page_count
                print(f"{book.__class__.__name__}: {book.title}, by {book.author}, Page Count: {book.page_count}")
            if isinstance(book, EBook):
                print(f"{book.__class__.__name__}: {book.title}, by {book.author}, File Size: {book.file_size}MB")
            elif isinstance(book, Book):  # base class
                print(f"{book.__class__.__name__}: {book.title}, by {book.author}")

def main():
    # Create a Library instance
    my_library = Library()

    # Create instances of each type of book
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    # Add books to the library
    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    # List all books in the library
    my_library.list_books()

if __name__ == "__main__":
    main()