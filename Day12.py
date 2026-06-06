# MATCH CASE IN PYTHON
# Match case is a new feature in python 3.10 and above
# It is used to match a value against a pattern and execute a block of code based on the match
# The syntax of match case is as follows:

X = int(input("Enter a number: "))

match X:
    case 1:
        print("You entered 1")
    case 2:
        print("You entered 2")
    case 3:
        print("You entered 3")
    case _:
        print("You entered a number other than 1,2,3")