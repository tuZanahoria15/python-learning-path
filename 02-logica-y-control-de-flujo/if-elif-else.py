# Variables
x = 5
y = 3
z = 1

# Simple if statement
if x > y:
    print ("5 is greater than 3")

if y > x:
    print ("3 is greater than 5")



# Using elif and else
if x > y:
    print ("5 is greater than 3")
elif x == y:
    print ("5 is equal to 3")
else:
    print ("5 is less than 3")


# Using multiple conditions
if x > y and x > z:
    print ("x is the greatest")
elif x == y:
    print ("x is equal to y")
else:
    print ("None of the conditions are true")




a = "Python"
b = "JavaScript"
c = "Python"

# Nested if statements
if a == c:
    if a != b:
        print ("a is equal to c, but not equal to b")
    else:
        print("This is an inner else exit")
else:
    print ("a is not equal to c")



"""
Avoiding empty if statements

In some cases, you may want to have an if statement 
without any code inside it.
"""
e = 10
f = 10

if e == f:
    #I can use a pass statement to indicate that I will handle this case later
    pass
