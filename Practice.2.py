# Practice Problem: Display only those characters which are present at an even index number in given string.
word = "pynative"
size = len(word)
for i in range(0,size-1,2):
    print(word[i])
    # print(size)