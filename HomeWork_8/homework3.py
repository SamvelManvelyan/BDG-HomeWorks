# Exercise 3:
# Write a Python function that takes two sets as input and returns a new set containing
# elements that are present in the first set but not in the second set.


input1 = set(input("Enter Word 1  "))
input2 = set(input("Enter Word 2  "))
pat = input1 - input2

print(pat)

