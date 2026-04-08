"""Simple Herence and Polymorphism example with a Library System"""

from typing import Protocol
from main import Book

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


# Aplying Instances
student = Student("Fernando", "21630243", "Computer Science")
student1 = Student("Juan Carlos", "21630237", "Computer Science")
teacher = Teacher("Ing. Selene", "86430987")

# This cannot be added into the list because does not implement the Borrowable protocol
book = Book("Python Fundamentals", "John Doe", "978-1234567890", True)

# Polimorphism: Pylance recognizes book as an error because it does not have the method request_book, but since it implements the Borrowable protocol, it can be used in the same way as the other classes that implement the protocol.
users: list[Borrowable] = [student, student1, teacher]

for user in users:
    print(user.request_book("Python Fundamentals"))

