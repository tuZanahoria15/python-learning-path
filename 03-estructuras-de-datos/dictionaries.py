"""
Dictionary:
It is used to store data in key-value pairs. 
It is unordered, changeable, and does not allow duplicates.
"""

# Collection of dictionaries key-value pairs
car = {
    "brand": "Toyota",
    "model": "Camry",
    "year": 2020
}

print(car)  # Output: {'brand': 'Toyota', 'model': 'Camry', 'year': 2020}



# How to pick impartially a value from the dictionary
print(car["brand"])  # Output: Toyota
print(car["model"]) # Output: Camry
print(car["year"]) # Output: 2020

# We can also use the get() method to access values in a dictionary.
print(car.get("brand"))  # Output: Toyota



# Get only the keys of the dictionary
print(car.keys())  # Output: dict_keys(['brand', 'model', 'year'])

# Get only the values of the dictionary
print(car.values())  # Output: dict_values(['Toyota', 'Camry', 202



# How to verify if a key exists in the dictionary
# Remember, it is case-sensitive, so "Brand" is different from "brand"
if "brand" in car:
    print("Brand is present in the dictionary")  # Output: Brand is present in the dictionary



# Replacing the value of an existing key in the dictionary
car["model"] = "Corolla"  # Changing the value of the "model"
car["year"] = 2021  # Changing the value of the "year"
print(car)  # Updated dictionary



"""
Methods in dictionaries:
* update() - Updates the dictionary with the specified key-value pairs. 
If a key already exists, its value will be updated.

* pop() - Removes the specified key and returns its value. Raises KeyError if the key is not found.
* popitem() - Removes and returns the last inserted key-value pair as a tuple. Raises KeyError if the dictionary is empty.
"""

car.update({"color": "red", "feature": "leather seats"})  # Adding multiple new key-value pair to the dictionary
print(car)  # Output: {'brand': 'Toyota', 'model': 'Corolla', 'year': 2021, 'color': 'red', 'feature': 'leather seats'}

car.pop("feature")  # This will remove the "feature" key and its value from the dictionary
print(car)  # Output: {'brand': 'Toyota', 'model': 'Corolla', 'year': 2021, 'color': 'red'}

car.popitem()  # This will remove the last inserted key-value pair from the dictionary
print(car)  # Output: {'brand': 'Toyota', 'model': 'Corolla

car.clear()  # This will remove all items from the dictionary, leaving it empty
print(car)  # Output: {} because the dictionary is now empty

print("__________________________________________________")



# Using for loop to iterate through a dictionary
newCar = {
    "brand": "Honda",
    "model": "Civic",
    "year": 2022,
    "color": "blue",
    "feature": "sunroof"
}

for key in newCar:
    print(key)  # Output: brand, model, year, color, feature (order may vary because dictionaries are unordered)

print("____________")

for value in newCar.values():
    print(value)  # Output: Honda, Civic, 2022, blue, sunroof (order may vary because dictionaries are unordered)

print("____________")

# To get both keys and values, we can use the items() method which returns a view object that displays a list of dictionary's key-value tuple pairs.
for key, value in newCar.items():
    print(key, value)  # Output: brand Honda, model Civic, year 2022, color blue, feature sunroof (order may vary because dictionaries are unordered)



"""
Nested dictionaries:
Are dictionaries that contain other dictionaries as values. 
They are useful for representing complex data structures.

Also known as directed graphs, they are a way to represent hierarchical data.
"""

# Each child is a dictionary with its own key-value pairs, and the main dictionary "family" contains these child dictionaries as values.
family = {
    "child1": {
        "name": "Fernando",
        "age": 23
    },
    "child2": {
        "name": "Juan Carlos",
        "age": 22
    },
    "child3": {
        "name": "Sergio",
        "age": 28
    }
}

# To access the values in a nested dictionary, we can use multiple keys. 
# For example, to access the name of child1, we can use:
print(family["child1"]["name"])  # Output: Fernando