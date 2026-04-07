# Defining classes in Python
class Book:

    # Methods are functions defined inside a class
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


my_book = Book("100 Years of Solitude", "Gabriel Garcia Marquez", "978-0060883287", True)
other_book = Book("The little prince", "Antoine de Saint-Exupéry", "978-0156012195", False)

my_book.set_times_borrowed(10)
print(f"Times borrowed: {my_book.get_times_borrowed()}")

catalogue = [my_book, other_book]

for book in catalogue:
    print(book)

