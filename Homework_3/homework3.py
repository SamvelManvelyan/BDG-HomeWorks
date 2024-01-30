# Write a Python program to remove the n-th index character from a nonempty string.
# Example:
# Sample string: ‘abcdefgh’
# n - 3
# Expected result: abcefgh


sample_string = "abcdefgh"
n = 3

result = sample_string[:n] + sample_string[4:8]

print(result)


