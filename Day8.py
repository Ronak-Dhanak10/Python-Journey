# STRING SLICING IN PYTHON
# String slicing is the process of extracting a portion of a string using its index
str = " I LOVE TO EAT MANGOES VERY MUCH IN SUMMER "
print(len(str)) # This will return the length of the string
print(str[0:11]) # This will return the substring from index 0 to 10
print(str[11:21]) # This is slicing in python
for char in str:
    print(char) # This will print each character in the string on a new line
# print(len(str))
# NEGATIVE SLACING 
print(str[-17:-4])
print(len(str))
# LOGIC OF NEGATIVE INDEXING
# FIND THE LENGTH OF THE STRING
# SUBTRACT THE LENGTH OF THE STRING FROM THE INDEX TO GET THE NEGATIVE INDEX
# EXAMPLE:
# STRING = "HELLO WORLD"
# LENGTH OF STRING = 11
# PRINT(STRING[-6:-1])
# SO WHAT HAPPENS IS THAT THE INDEX -6 WILL BE EQUAL TO 11-6 = 5 AND THE INDEX -1 WILL BE EQUAL TO 11-1 = 10
# SO THE SUBSTRING WILL BE FROM INDEX 5 TO 9 WHICH IS "WORLD"