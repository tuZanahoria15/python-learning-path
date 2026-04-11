from typing import Protocol


class BookProtocol(Protocol):
    def borrow(self) -> str:
        """Method to borrow a book"""
        ...

    def return_book(self) -> str:
        """MMethod to return a book"""
        ...

    def calculate_loan_duration(self) -> str:
        """Calculates the loan duration"""
        ...

class Book:

    # The __init__ method is a special method that is called when an object is created from a class and allows the class to initialize the attributes of the class.
    def __init__(self, title, author, isbn, available):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available
        self.__times_borrowed = 0 

    """
    NOTES:
    1. The underscore before an attribute name indicates that it is intended to be a private attribute, meaning it should not be accessed directly from outside the class.
    2. Two underscores before an attribute name indicate that it is a private attribute that cannot be accessed directly from outside the class, and secures it from being accidentally modified or accessed.
    """
        
    # The __str__ method is a special method that defines how an object is represented as a string and returns it
    def __str__(self):
        return f"{self.title} by {self.author} is available: {self.available}"

    # Upcoming next, methods are functions defined inside a class
    def borrow(self):
        if self.available:
            self.available = False
            self.__times_borrowed += 1
            return f"'{self.title}' was borrowed successfully.\nTimes borrowed: {self.__times_borrowed}"
        return f"'{self.title}' is currently not available."

    def return_book(self):
        self.available = True
        return f"'{self.title}' was returned and is now available"
    
    def is_popular(self):
        return self.__times_borrowed >= 5
    
    # ENCAPSULATION WITH GETTERS AND SETTERS
    def get_times_borrowed(self): # This method allows us to access the private attribute __times_borrowed from outside the class
        return self.__times_borrowed
    
    def set_times_borrowed(self, times_borrowed): # This method allows us to set the value of the private attribute __times_borrowed from outside the class
        self.__times_borrowed = times_borrowed


# New Classes
class PhysicalBook(Book):
    def calculate_loan_duration(self):
        return "Loan duration for physical books is 7 days."
    
class EBook(Book):
    def calculate_loan_duration(self):
        return "Loan duration for e-books is 14 days."
 