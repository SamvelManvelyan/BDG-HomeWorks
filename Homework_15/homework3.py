# 3. Write a python program to add text to a file and display the text in python.txt.


with open('text2.txt', 'w') as file:
    file.write('Hayastan Yerevan ')

f = open("text2.txt" )
print(f.read())
