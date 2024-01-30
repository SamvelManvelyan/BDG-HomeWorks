# Exercise 3: Word Finder
# Write a program that takes a list of words and a target word as input.
# The program should find and print all words in the list that contain the
# target word. Use a for loop, the in operator, and an if statement to
# check if the target word is present in each word in the list.


input_words = ["Samvel", "Arman", "Meqena", "Yerevan", "Vanadzor", "Gyumri"]
input_target = input("Enter the target word: ")
matching_words = []
for word in input_words:
    if input_target in word:
        matching_words.append(word)

print("Words containing the target word: " , matching_words)