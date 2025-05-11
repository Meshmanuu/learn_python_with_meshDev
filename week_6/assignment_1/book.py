class Book:
    """Represents a book with its title, author, ISBN, and current page."""

    def __init__(self, title, author, isbn, total_pages):
        """
        Initializes a new Book object.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The International Standard Book Number.
            total_pages (int): The total number of pages in the book.
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.total_pages = total_pages
        self.current_page = 1  # Start at the first page
        self.is_open = False

    def open(self):
        """Opens the book."""
        if not self.is_open:
            self.is_open = True
            print(f"Opening '{self.title}'.")
        else:
            print(f"'{self.title}' is already open.")

    def close(self):
        """Closes the book."""
        if self.is_open:
            self.is_open = False
            print(f"Closing '{self.title}'.")
        else:
            print(f"'{self.title}' is already closed.")

    def turn_page(self, pages=1):
        """Turns the specified number of pages forward."""
        if self.is_open:
            if self.current_page + pages <= self.total_pages:
                self.current_page += pages
                print(f"Turned to page {self.current_page} of '{self.title}'.")
            else:
                self.current_page = self.total_pages
                print(f"Reached the end of '{self.title}' on page {self.current_page}.")
        else:
            print(f"Please open '{self.title}' first.")

    def go_to_page(self, page_number):
        """Goes directly to the specified page number."""
        if self.is_open:
            if 1 <= page_number <= self.total_pages:
                self.current_page = page_number
                print(f"Went to page {self.current_page} of '{self.title}'.")
            else:
                print(f"Invalid page number for '{self.title}'. It has {self.total_pages} pages.")
        else:
            print(f"Please open '{self.title}' first.")

# Creating instances of the Book class
the_alchemist = Book("The Alchemist", "Paulo Coelho", "978-0061122415", 197)
sapiens = Book("Sapiens: A Brief History of Humankind", "Yuval Noah Harari", "978-0062316097", 498)

the_alchemist.open()
the_alchemist.turn_page(50)
the_alchemist.go_to_page(100)
the_alchemist.close()

sapiens.open()
sapiens.turn_page(100)
sapiens.turn_page(500) # Will go to the last page
sapiens.close()