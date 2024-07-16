# library.py
import json
from book import Book

class Library:
    def __init__(self):
        self.books = []
        self.lent_books = []

    def add_book(self, book):
        self.books.append(book)
        self.save_state()

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                self.save_state()
                return True
        return False

    def lend_book(self, isbn, borrower):
        for book in self.books:
            if book.isbn == isbn:
                if book.quantity > 0:
                    book.quantity -= 1
                    self.lent_books.append((book, borrower))
                    self.save_state()
                    return True
                else:
                    print("Error: Not enough books available to lend.")
                    return False
        return False

    def return_book(self, isbn):
        for lent_book, borrower in self.lent_books:
            if lent_book.isbn == isbn:
                lent_book.quantity += 1
                self.lent_books.remove((lent_book, borrower))
                self.save_state()
                return True
        return False

    def search_books_by_title_or_isbn(self, search_term):
        results = []
        for book in self.books:
            if search_term.lower() in book.title.lower() or search_term.lower() == book.isbn.lower():
                results.append(book)
        return results

    def search_books_by_author(self, author):
        results = []
        for book in self.books:
            for a in book.authors:
                if author.lower() in a.lower():
                    results.append(book)
                    break
        return results

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book.display_info())

    def display_lent_books(self):
        if not self.lent_books:
            print("No books currently lent.")
        else:
            for book, borrower in self.lent_books:
                print(f"Title: {book.title} | Lent to: {borrower}")

    def save_state(self):
        data = {
            'books': [book.__dict__ for book in self.books],
            'lent_books': [(book.__dict__, borrower) for book, borrower in self.lent_books]
        }
        with open('data.json', 'w') as f:
            json.dump(data, f)

    def load_state(self):
        try:
            with open('data.json', 'r') as f:
                data = json.load(f)
                self.books = [Book(**book_data) for book_data in data['books']]
                self.lent_books = [(Book(**book_data), borrower) for book_data, borrower in data['lent_books']]
        except FileNotFoundError:
            # If file doesn't exist, start with empty state
            self.books = []
            self.lent_books = []
