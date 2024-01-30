# 4.Write a function display_words() in python to read text from a text file "example.txt",
# and display those words, which are less than 4 characters.


def display_words():
    f = open("text2.txt")
    print(f.read()[-4:])

display_words()