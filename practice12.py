# Practice Problem: Write a function to return True if the first and last number of a given list is the same. 
# If the numbers are different, return False.
def guess_number(guess_number):
    first_num = guess_number[0]
    last_num = guess_number[-1]
    if first_num == last_num:
        return True
    else:
        return False
x = [99, 22, 33, 44, 55, 66, 77, 88, 98]
print(guess_number(x))
y = [16, 22, 33, 44, 55, 66, 77, 88, 99, 11]
print(guess_number(y))