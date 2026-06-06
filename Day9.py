# METHODS IN STRINGS
# A method is a function that is associated with an object and can be called on that object
# String methods are built-in functions that can be used to manipulate strings
# Some common string methods are:
# 1. upper() - This method converts all the characters in a string to uppercase
# 2. lower() - This method converts all the characters in a string to lowercase
# 3. strip() - This method removes any leading and trailing whitespace from a string
# 4. replace() - This method replaces a specified substring with another substring in a string
# 5. split() - This method splits a string into a list of substrings based on a specified delimiter
# 6. join() - This method joins a list of strings into a single string using a specified delimiter
# 7. find() - This method returns the index of the first occurrence of a specified
# substring in a string, or -1 if the substring is not found
# 8. count() - This method returns the number of occurrences of a specified substring in a string
# 9. isalpha() - This method returns True if all the characters in a string are alphabetic, and False otherwise
# 10. isdigit() - This method returns True if all the characters in a string are digits, and False otherwise
# 11. isspace() - This method returns True if all the characters in a string
# are whitespace, and False otherwise
# 12. title() - This method converts the first character of each word in a string to uppercase and the rest of the characters to lowercase
# 13. capitalize() - This method converts the first character of a string to uppercase and the rest of the characters to lowercase
# 14. swapcase() - This method converts all the uppercase characters in a string to lowercase and all the lowercase characters to uppercase
# 15. startswith() - This method returns True if a string starts with a specified
# 16. endswith() - This method returns True if a string ends with a specified substring, and False otherwise
# 17. center() - This method returns a centered string of a specified width, padded with a specified character (default is space)
st = "@@@@@@@@@@RONAK@@@@@@@@@@" 
print(st.upper()) # This will convert all the characters in the string to uppercase
print(st.lower()) # This will convert all the characters in the string to lowercase
print(st.strip("@")) # This will remove any leading and trailing "@" from the string
print(st.replace("RONAK","OM")) # This will replace "RONAK" with "OM" in the string
print(st.split("@")) # This will split the string into a list of substrings based on
# the "@" delimiter
print("-".join(st.split("@"))) # This will join the list of substrings into a single string using the "-" delimiter
print(st.find("RONAK")) # This will return the index of the first occurrence of "RONAK" in the string, or -1 if "RONAK" is not found
print(st.count("RONAK")) # This will return the number of occurrences of "RONAK" in the string
print(st.isalpha()) # This will return False because the string contains "@" which is not an alphabetic character
print(st.isdigit()) # This will return False because the string contains "@" which is not   a digit character
print(st.isspace()) # This will return False because the string contains "@" which is not a whitespace character
print(st.title()) # This will convert the first character of each word in the string to uppercase and the rest of the characters to lowercase
print(st.capitalize()) # This will convert the first character of the string to uppercase and the rest
# of the characters to lowercase
print(st.swapcase()) # This will convert all the uppercase characters in the string to lowercase and all the lowercase characters to uppercas                
print(st.center(50,"*")) # This will return a centered string of width 50, padded with "*" characters
print(st.encode("utf-8")) # This will return a bytes object containing the encoded version of the string
print(st.endswith("RONAK")) # This will return False because the string does not end with "RONAK"