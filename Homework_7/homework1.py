# 1.Arrange
# Arrange string characters such that lowercase letters should come first
# Sample Input Sample Output
#                                PyNaTive            yaivePNT


word = "PyNaTive"
# new_word = word.replace("PyNaTive","yaivePNT")
lowercase = []
not_lower = []

for x in word:
    if x.islower():
        lowercase.append(x)
    elif x.isupper():
        not_lower.append(x)
result = "".join(lowercase) + "".join(not_lower)
print(result)


