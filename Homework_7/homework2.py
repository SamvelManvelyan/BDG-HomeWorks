# 2.Count
# Count all letters, digits, and special symbols from a given string
# Sample Input Sample Output
# P@#yn26at^&i5ve     Total counts of chars, digits, and
# symbols
# chars = 8
# digits = 3
# symbol = 4

word = "P@#yn26at^&i5ve"

chars = []
digits = []
sympols = []

for x in word:
    if x.isdigit():
        digits.append(x)
    elif x.isupper() or x.islower():
        chars.append(x)
    else:
        sympols.append(x)
print(len(chars))
print(len(digits))
print(len(sympols))