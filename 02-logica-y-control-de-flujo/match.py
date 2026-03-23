"""
Match statement in Python (added in Python 3.10)
is a powerful control flow structure that allows you 
to compare a value against multiple patterns and execute code 
based on which pattern matches. 

It is similar to switch-case statements found in other 
programming languages (like Java) but with more 
advanced pattern matching capabilities.
"""

# Variable
day = 1

# Match statement to determine the day of the week based on the value of 'day'
match day:
    case 1:
        print ("Monday")
    case 2:
        print ("Tuesday")
    case 3:
        print ("Wednesday")
    case 4:
        print ("Thursday")
    case 5:
        print ("Friday")
    case 6:
        print ("Saturday")
    case 7:
        print ("Sunday")
    case _: # It is used as a wildcard to match any value that hasn't been matched by the previous cases
        print ("Invalid day number")



"""
EXCERCISE:
The user inputs a string representing a day of the week (e.g., "Monday", "Tuesday", etc.)
and the program uses a match statement to print 
the corresponding activity plan for that day of the week. 
"""

activity_plan = input("Enter a day of the week: ").lower() # Convert the input to lowercase to make the matching case-insensitive
match activity_plan:
    case "monday":
        print ("Go to the gym")
    case "tuesday":
        print ("Attend a cooking class")
    case "wednesday":
        print ("Go for a hike")
    case "thursday":
        print ("Have a movie night")
    case "friday":
        print ("Go out with friends")
    case "saturday":
        print ("Relax at home")
    case "sunday":
        print ("Play videogames")
    case _:
        print ("*ERROR* You may have entered an invalid day of the week. Please try again.")
