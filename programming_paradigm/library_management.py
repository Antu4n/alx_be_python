class Book:
    """
    A class to represent a book in the library system.
    
    Attributes:
        title (str): The title of the book (public)
        author (str): The author of the book (public)
        _is_checked_out (bool): The availability status of the book (private)
    """
    
    def __init__(self, title, author):
        """
        Initialize a new book with title and author.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
        """
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute - book starts as available
    
    def check_out(self):
        """
        Check out the book if it's available.
        
        Returns:
            bool: True if book was successfully checked out, False if already checked out
        """
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    def return_book(self):
        """
        Return the book if it's currently checked out.
        
        Returns:
            bool: True if book was successfully returned, False if not checked out
        """
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
    
    def is_available(self):
        """
        Check if the book is available for checkout.
        
        Returns:
            bool: True if book is available, False if checked out
        """
        return not self._is_checked_out
    
    def __str__(self):
        """
        String representation of the book.
        
        Returns:
            str: Formatted string showing title and author
        """
        return f"{self.title} by {self.author}"


class Library:
    """
    A class to represent a library that manages a collection of books.
    
    Attributes:
        _books (list): Private list to store Book instances
    """
    
    def __init__(self):
        """Initialize an empty library."""
        self._books = []  # Private attribute to store books
    
    def add_book(self, book):
        """
        Add a book to the library collection.
        
        Args:
            book (Book): An instance of the Book class to add to the library
        """
        if isinstance(book, Book):
            self._books.append(book)
        else:
            print("Error: Only Book instances can be added to the library.")
    
    def check_out_book(self, title):
        """
        Check out a book by its title.
        
        Args:
            title (str): The title of the book to check out
            
        Returns:
            bool: True if book was found and checked out, False otherwise
        """
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"Successfully checked out '{title}'")
                    return True
                else:
                    print(f"'{title}' is already checked out.")
                    return False
        
        print(f"Book '{title}' not found in the library.")
        return False
    
    def return_book(self, title):
        """
        Return a book by its title.
        
        Args:
            title (str): The title of the book to return
            
        Returns:
            bool: True if book was found and returned, False otherwise
        """
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"Successfully returned '{title}'")
                    return True
                else:
                    print(f"'{title}' was not checked out.")
                    return False
        
        print(f"Book '{title}' not found in the library.")
        return False
    
    def list_available_books(self):
        """
        Display all available books in the library.
        """
        available_books = [book for book in self._books if book.is_available()]
        
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No books are currently available.")
    
    def list_all_books(self):
        """
        Display all books in the library with their status.
        """
        if self._books:
            for book in self._books:
                status = "Available" if book.is_available() else "Checked Out"
                print(f"{book} - {status}")
        else:
            print("The library has no books.")
    
    def get_book_count(self):
        """
        Get the total number of books in the library.
        
        Returns:
            int: Total number of books
        """
        return len(self._books)
    
    def get_available_count(self):
        """
        Get the number of available books in the library.
        
        Returns:
            int: Number of available books
        """
        return len([book for book in self._books if book.is_available()])
