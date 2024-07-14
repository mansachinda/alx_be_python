"""
Program to Solidify understanding of basic OOP concepts in Python by implementing a system
that tracks books in a library, focusing on classes, object instantiation, and method invocation.
"""

# Create 'Book' class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

# 'check_out_book' function with 'Book' class
    def check_out_book(self):
        if self.title == self.title:
            self._is_checked_out == True
            return True
        else:
            return False

# 'return_book' function with 'Book' class
    def return_book(self):
        if self.title == self.title:
            self._is_checked_out == False
            return True
        else:
            return False


class Library:
    def __init__(self):
        """
        This is a Private attributes of two lists.
        """
        self._books = []
        self._checked_out_books = []

    def add_book(self, book):
        """
        This adds a book to the list of books in library.
        """
        self._books.append(book)
        return

    def check_out_book(self, title):
        """
        This Loops through the list.
        Then if title matches a title, remove _books list and append it to _checked_out_books.
        Then Break the loop and print the remaining books in the _books list.
        """

        for book in self._books:
            if book.title == title:
                book._is_checked_out = True
                self._books.remove(book)
                self._checked_out_books.append(book)
                break
        for remain in self._books:
            print(f"{remain.title} by {remain.author}")

    def return_book(self, title):
        """
        This Loops through _checked_out_books list and finds a match to the title.
        Then adds the book to _books list and removes it from _checked_out_books
        Then prints the updated list apprioprately.
        """
        for book in self._checked_out_books:
            if book.title == title:
                book._is_checked_out = False
                self._books.append(book)
                self._checked_out_books.remove(book)
                return
            print(f"Book {title} is not available")
        for new_list in self._books:
            print(f"{new_list.title} by {new_list.author}")

    def list_available_books(self):
        for book in self._books:
            print(f"{book.title} by {book.author}")
