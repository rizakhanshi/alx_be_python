class Book:
    """Represents a single book in the library."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def check_out(self):
        """Mark the book as not available."""
        self.available = False

    def return_book(self):
        """Mark the book as available."""
        self.available = True

    def is_available(self):
        """Return True if the book is available."""
        return self.available

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    """Manages a collection of books."""

    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Add a book to the library."""
        self.books.append(book)

    def check_out_book(self, title):
        """Check out a book by title."""
        for book in self.books:
            if book.title == title and book.is_available():
                book.check_out()
                return

    def return_book(self, title):
        """Return a book by title."""
        for book in self.books:
            if book.title == title and not book.is_available():
                book.return_book()
                return

    def list_available_books(self):
        """List all available books."""
        for b
