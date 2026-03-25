"""
Tuples:
A tuple is a collection which is ordered and unchangeable. 
In Python tuples are written with round brackets.
"""

# Index            0           1          2        3
technologies = ("Python", "JavaScript", "C++", "Python")

print(technologies)
print(technologies[1])  # Output: JavaScript
print(len(technologies))  # Output: 4
print(type(technologies))  # Output: <class 'tuple'>



"""
In order to declare a one element tuple, 
you need to include a comma after the element, 
otherwise it will be treated as a string.
"""
one_element_tuple = ("Python",)  # Note the comma after "Python"
print(one_element_tuple)  # Output: ('Python',)

# Tuples can contain items of different data types
person = ("Fernando", 23, True)
print(person)
print(type(person))  # Output: <class 'tuple'>


# How to unbox a tuple
x, y, z = person
print(x)  # Output: Fernando
print(y)  # Output: 23
print(z)  # Output: True


# Tuples can be concatenated using the + operator
tuple1 = (1, 2, 3)
tuple2 = (3, 4, 5)
tuple3 = tuple1 + tuple2 # Duplicates are allowed in tuples
print(tuple3)  # Output: (1, 2, 3, 3, 4, 5)


# Tuples can be repeated using the * operator
print(person * 2)  # Output: ('Fernando', 23, True, 'Fernando', 23, True)


# Using for loop to iterate through a tuple
for item in person:
    print(item)

print("_____________________________________")

"""
How to convert a tuple to a list and vice versa:

* In order to convert a tuple to a list, it is needed 
to do a cast using the list() function.

* In order to convert a list to a tuple, it is needed 
to do a cast using the tuple() function.

This is useful because tuples are immutable, 
meaning you cannot modify them after they have been created.
"""

edible_tuple = ("apple", "banana", "pear")
newlist = list(edible_tuple)  # Convert tuple to list
newlist.append("orange")  # Now we can modify the list whatever we want
edible_tuple = tuple(newlist)  # Convert list back to tuple

print(edible_tuple)  # Output: ('apple', 'banana', 'pear', 'orange')
