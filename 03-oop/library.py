# Composition: A library has books and users, but books and users can exist independently of the library.
# This is an example of composition because the library is composed of books and users, but they are not dependent on the library to exist.
class Library:
    def __init__(self, name) -> None:
        self.name = name
        self.books = [] # Library HAS books
        self.users = [] # Library HAS users

    def available_books(self):
        return [book.title for book in self.books if book.available]