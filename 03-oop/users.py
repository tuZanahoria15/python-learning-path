"""Simple Herence and Polymorphism example with a Library System"""

from typing import Protocol


class Borrowable(Protocol):
    def request_book(self, title: str) -> str:
        """This method should implement the logic for requesting a book."""
        ...


class User:
    def __init__(self, name, ID_card):
        self.name = name
        self.ID_card = ID_card
        self.borrowed_books = []

    def request_book(self, title):
        return f"The '{title}' has been requested."


class Student(User):
    def __init__(self, name, ID_card , major):
        # Super() method allows us to call the __init__ method of the parent class (User) from the child class (Student) and initialize the attributes of the parent class in the child class.
        super().__init__(name, ID_card)

        # Child class (Student) has its own attributes
        self.major = major
        self.book_limit = 3

    # Overwrite method
    def request_book(self, title):
        if len(self.borrowed_books) < self.book_limit:
            self.borrowed_books.append(title)
            return f"--> STATUS: Authorized book loan for:\n'{title}'\n"
        else:
            return f"--> ADVICE: Limit reached!\n{self.name} cannot borrow more than {self.book_limit} books."


class Teacher(User):
    def __init__(self, name, ID_card):
        super().__init__(name, ID_card)

        # Child class (Teacher) has its own attributes
        self.book_limit = None

    
    # Overwrite method
    def request_book(self, title):
        return f"--> STATUS: Authorized book loan for:\n'{title}'\n"




