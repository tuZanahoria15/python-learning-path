"""
Sets:
A set is a collection which is unordered and unindexed.
In Python sets are written with curly brackets.
"""

# Sets cannot be duplicated, meaning that they cannot contain duplicate items.
fruits = {"apple", "banana", "pear", "apple"}
print(fruits)
print(type(fruits))  # Output: <class 'set'>
print(len(fruits))  # Output: 3 because "apple" is duplicated and ignored in the set


# Sets can contain items of different data types
mySet = {"Dog", 7, True}
print(mySet)
print(type(mySet))  # Output: <class 'set'>


# For loop can be used to iterate through a set
for item in mySet:
    print(item) # Output: True, Dog, 7 (order may vary because sets are unordered)


# Looking for an item using in/not in
print("apple" in fruits) # Output: 
print("grape" not in fruits) # Output: 



"""
Methods in sets:
add() - Adds an element to the set
update() - Updates the set with the union of this set and others
remove() - Removes the specified element from the set
discard() - Removes the specified element from the set if it is present
prop()* - Removes randomly an element from the set and returns it. Raises KeyError if the set is empty
"""

# Remember, sets are unordered, so the order of items may vary when printed
fruits.add("grape")
print(fruits) # Output: {'banana', 'grape', 'apple', 'pear'}

# Also, update() can add lists, tuples, sets, or dictionaries to a set. It will add each element of the iterable to the set.
tropical = {"mango", "papaya", "pineapple"}
fruits.update(tropical)



# Discard also works like remove, but it does not raise an error if the item is not found in the set. 
# This can be useful when you want to remove an item without worrying about whether it exists in the set or not.

fruits.remove("banana")  # This will remove "banana" from the set
fruits.discard("grape")  # This will remove "grape" from the set if it is present, otherwise it does nothing
fruits.clear()  # This will remove all items from the set, leaving it empty
print(fruits) # Output: set() because the set is now empty



"""Operations on sets: 
* union() - Returns a set containing the union of sets
* intersection() - Returns a set containing the intersection of sets
* difference() - Returns a set containing the difference of sets
"""

a = {"a", "b", "c"}
b = {"b", "c", "d"}

# Union
u = a.union(b)
print(u)  # Output: {'a', 'b', 'c', 'd'}

# Intersection
i = a.intersection(b)
print(i)  # Output: {'b', 'c'}

# Difference
d = a.difference(b)
print(d)  # Output: {'a'}
