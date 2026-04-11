from users import Student, Teacher, Borrowable
from books import PhysicalBook
from library import Library


# Instance a new library and add the books to it
library = Library("Platzi Library")

# Aplying Instances
student = Student("Fernando", "21630243", "Computer Science")
student1 = Student("Juan Carlos", "21630237", "Computer Science")
teacher = Teacher("Ing. Selene", "86430987")

# Polimorphism: Pylance recognizes book as an error because it does not have the method request_book, but since it implements the Borrowable protocol, it can be used in the same way as the other classes that implement the protocol.
users: list[Borrowable] = [student, student1, teacher]

my_book = PhysicalBook(
    "100 years of solitude",
    "Gabriel García Márquez",
    "978-1234567890",
    True,
)

other_book = PhysicalBook(
    "The Little Prince",
    "Antoine de Saint-Exupéry",
    "978-0987654321",
    True,
)

not_available_book = PhysicalBook(
    "The Great Gatsby",
    "F. Scott Fitzgerald",
    "978-1122334455",
    False,
)


library.books = [my_book, not_available_book, other_book]

print(library.books)