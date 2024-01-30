# Exercise 2: Vowel Counter
# Write a program that takes a string as input and counts the
# number of vowels (a, e, i, o, u) in the string. Use a for
# loop, an if statement, and the in operator to check if a
# character is a vowel.

strx = input("Enter a string:  ")
vowels = "aeiou"
vowel_count = 0
for x in strx:
    if x in vowels:
        vowel_count += 1

print("Number of vowels:", vowel_count)