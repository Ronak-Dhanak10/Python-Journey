# Practice Problem: Write a function to remove characters from a string 
# starting from index 0 up to n and return a new string.
def remove_str(word,n):
 res = word[n:]
 return res
print(remove_str("Whereareyougoing",8))
