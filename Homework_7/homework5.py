# 3)Write a Python program that input a sentence and return the longest word and the length of the longest one.
my_input = input("Enter your word  " )
word = my_input.split(" ")
long_check = word[0]
long_word = []
for x in word:
    if len(long_check) <= len(x):
        long_word = x
print("The long word is:" ,long_word , "Leght is " , len(long_word) )