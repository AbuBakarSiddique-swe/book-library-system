# utils.py

def get_input(prompt):
    return input(prompt).strip()

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a floating-point number.")

def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")

def display_search_results(results):
    if results:
        for book in results:
            print(book.display_info())
    else:
        print("No books found.")
