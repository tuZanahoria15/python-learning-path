# It is possible to assign multiple variables in one line in Python.
x, y, z = "Apple", "Banana", "Cherry"

print(x, y, z) #Prints the values of x, y, and z

a = b =c = "Lime"

print(a, b, c) #Prints just the value of a, b, and c, which are all the same.


"""
Now let's do concatenation with multiple assignment.
"""
print ("My favorite fruit is: " + x)
print ("Also, I like: " + y + " and " + z)


"""
An example of arithmetic operation.
"""
d = 5
e = 6
print(d + e) #Prints the sum of d and e, which is 11.


"""
If we want to perform an concatenation.
"""
print("The sum of " + str(d) + " and " + str(e) + " is: " + str(d + e))
# We must convert the integers to strings using the str() function in order to concatenate them with the other strings.