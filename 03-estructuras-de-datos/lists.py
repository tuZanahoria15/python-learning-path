"""
Lists:
A list is a collection of items that are ordered and changeable. 
Lists are written with square brackets [] and can contain items 
of different data types, including other lists. 

Lists are mutable, meaning you can modify them after they have been created.
"""

# It is possible to have lists with different data types
List = ["Fernando", 15, True]
print(type(List))  # Output: <class 'list'>



# Index     0         1         2
fruits = ["apple", "banana", "pear"]
print(fruits)
print(type(fruits))

# Accessing list items
print(fruits[0])  # Output: apple

# Modifying list items
fruits[1] = "orange" 
print(fruits)  # Output: ['apple', 'orange', 'pear']



"""
Some properties of lists
"""
# Len() function can be used to get the number of items in a list
print(len(fruits))  # Output: 3

# Range of indexes can be specified to access a subset of the list
print(fruits[0:2])  # Output: ['apple', 'orange']

# Search for an item in the list using the 'in' keyword
if "apple" in fruits:
    print("Yes, 'apple' is in the list of fruits.")  



"""
Methods for lists:
- append(): Adds an item to the end of the list.
- insert(): Adds an item at a specified index.
- remove(): Removes the first occurrence of a specified item.
- pop(): Removes an item at a specified index and returns it.
- sort(): Sorts the items of the list in place.
- reverse(): Reverses the order of the items in the list.
- 
"""

# Index       0       1       2
vehicles = ["car", "bike", "plane"]

# Using append() to add an item to the END of the list
vehicles.append("boat")
print(vehicles)  # Output: ['car', 'bike', 'plane', 'boat']


# Using insert() to add an item at a specified index
vehicles.insert(1, "bus")
print(vehicles)  # Output: ['car', 'bus', 'bike', 'plane', 'boat']


# Using remove() to remove the first occurrence of a specified item
vehicles.remove("bike")
print(vehicles)  # Output: ['car', 'bus', 'plane', 'boat']


# Using pop() to remove an item at a specified index and return it
vehicles.pop(2)
print(vehicles)  # Output: ['car', 'bus', 'boat']


# Using sort() to sort the items of the list in place
vehicles.sort()
print(vehicles)  # Output: ['boat', 'bus', 'car']


# Using reverse() to reverse the order of the items in the list
vehicles.reverse()
print(vehicles)  # Output: ['boat', 'bus', 'car']


"""
Join Lists:
- The + operator can be used to concatenate two lists.
- The extend() method can be used to add the items of one list to the end of another list.

"""

collection1 = ["a", "b", "c"]
collection2 = [1, 2, 3]

# Using the + operator to concatenate two lists
combined_collection = collection1 + collection2

collection1.extend(collection2)
print(collection1)  # Output: ['a', 'b', 'c', 1, 2, 3]