# 2. Write a function in Python to count and display the total number of words in a text file.

file = open("text.txt", "rt")
txt = file.read()
words = txt.split()
print(' words in file :', len(words))