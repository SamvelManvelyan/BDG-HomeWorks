# Exercise 4: Palindrome Checker
# Write a program that prompts the user to enter a word and checks if it is
# a palindrome. A palindrome is a word that reads the same backward as
# forward. Use string slicing and an if-else statement to compare the
# original word with its reverse.
# Prompt the user to enter a word


user_input = input("Enter a word: ")
tars_word = user_input[::-1]
if user_input == tars_word:
    print(user_input," is a palindrome")
else:
    print(user_input," is not a palindrome.")