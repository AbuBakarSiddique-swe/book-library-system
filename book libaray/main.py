# main.py
from library import Library
from book import Book
import utils

def main():
    library = Library()
    library.load_state()

    while True:
        print("\n==== Library Management System ====")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search books by title or ISBN")
        print("4. Search books by author")
        print("5. Display all books")
        print("6. Display lent books")
        print("7. Lent a book")
        print("8. Return a book")
        print("9. Exit")

        choice = utils.get_input("Enter your choice: ")

        if choice == '1':
            title = utils.get_input("Enter title: ")
            authors = utils.get_input("Enter authors (comma separated): ").split(',')
            isbn = utils.get_input("Enter ISBN: ")
            year = utils.get_input("Enter year: ")
            price = utils.get_float_input("Enter price: ")
            quantity = utils.get_int_input("Enter quantity: ")
            book = Book(title, authors, isbn, year, price, quantity)
            library.add_book(book)

        elif choice == '2':
            isbn = utils.get_input("Enter ISBN of the book to remove: ")
            if library.remove_book(isbn):
                print("Book removed successfully.")
            else:
                print("Error: Book not found or unable to remove.")

        elif choice == '3':
            search_term = utils.get_input("Enter title or ISBN to search: ")
            results = library.search_books_by_title_or_isbn(search_term)
            utils.display_search_results(results)

        elif choice == '4':
            author = utils.get_input("Enter author name to search: ")
            results = library.search_books_by_author(author)
            utils.display_search_results(results)

        elif choice == '5':
            library.display_books()

        elif choice == '6':
            library.display_lent_books()

        elif choice == '7':
            isbn = utils.get_input("Enter ISBN of the book to lend: ")
            borrower = utils.get_input("Enter borrower's name: ")
            if library.lend_book(isbn, borrower):
                print("Book lent successfully.")
            else:
                print("Error: Unable to lend book.")

        elif choice == '8':
            isbn = utils.get_input("Enter ISBN of the book to return: ")
            if library.return_book(isbn):
                print("Book returned successfully.")
            else:
                print("Error: Unable to return book.")

        elif choice == '9':
            print("Saving and exiting program.")
            library.save_state()
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
