# 5. Write a python program to read a file, a.txt line by line.
file = open("text.txt", "rt")
txt = file.read()
words = txt.split('\n')
print('line in  file :', len(words))

