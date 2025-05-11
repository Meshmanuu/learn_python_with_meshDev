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
        self.current_page = 1
        self.is_open = False

    def open(self):
        if not self.is_open:
            self.is_open = True
            print(f"Opening '{self.title}'.")
        else:
            print(f"'{self.title}' is already open.")

    def close(self):
        if self.is_open:
            self.is_open = False
            print(f"Closing '{self.title}'.")
        else:
            print(f"'{self.title}' is already closed.")

    def turn_page(self, pages=1):
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
        if self.is_open:
            if 1 <= page_number <= self.total_pages:
                self.current_page = page_number
                print(f"Went to page {self.current_page} of '{self.title}'.")
            else:
                print(f"Invalid page number for '{self.title}'. It has {self.total_pages} pages.")
        else:
            print(f"Please open '{self.title}' first.")


class EBook(Book):
    """Represents an electronic book."""

    def __init__(self, title, author, isbn, total_pages, file_format):
        super().__init__(title, author, isbn, total_pages)
        self.file_format = file_format
        self.battery_percentage = 100

    def read(self):
        if self.battery_percentage > 0:
            self.open()
            print(f"Reading '{self.title}' in {self.file_format} format.")
        else:
            print(f"Battery is low. Please charge your device to read '{self.title}'.")

    def charge(self, percentage):
        self.battery_percentage = min(100, self.battery_percentage + percentage)
        print(f"Charging '{self.title}'. Battery level: {self.battery_percentage}%")


if __name__ == "__main__":
    the_alchemist = Book("The Alchemist", "Paulo Coelho", "978-0061122415", 197)
    sapiens_ebook = EBook("Sapiens", "Yuval Noah Harari", "978-0062316097", 498, "EPUB")

    the_alchemist.open()
    the_alchemist.turn_page(25)
    the_alchemist.close()

    sapiens_ebook.read()
    sapiens_ebook.turn_page(100)
    sapiens_ebook.charge(50)
    sapiens_ebook.close()