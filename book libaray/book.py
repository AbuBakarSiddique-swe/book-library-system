# book.py

class Book:
    def __init__(self, title, authors, isbn, year, price, quantity):
        self.title = title
        self.authors = authors
        self.isbn = isbn
        self.year = year
        self.price = price
        self.quantity = quantity

    def display_info(self):
        authors_str = ', '.join(self.authors)
        return f"Title: {self.title}\nAuthors: {authors_str}\nISBN: {self.isbn}\nYear: {self.year}\nPrice: ${self.price}\nQuantity: {self.quantity}\n"
