# 3.Balance
# Write a program to check if two strings are balanced. For example, strings s1 and
# s2 are balanced if all the characters in the s1 are present in s2. The character’s
# position doesn’t matter.
# Sample Input Sample Output
# s1 = "Yn"
# s2 = "PYnative"
# True
# s1 = "Ynf"
# s2 = "PYnative"
# False

word1 = "Yna"
word2 = "PYnative"

for x in word1:
    if x in word2:
        result = True
    else:
        result = False

print(result)




