# 4. Write a Python program to change a given string to a new string where the first and last chars
# have been exchanged.
# Example:
# Sample: ‘abcdefgh’
# Expected: ‘hbcdefga’


sample_string = 'abcdefgh'
sliced_string = sample_string[1:7]
result = "h" + sliced_string + "a"


