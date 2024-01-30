# 9. Append new string in the middle of a given (even number of characters) string
# Example:
# Sample = ‘python’
# new_string = ‘new’
# Expected ‘pytnewhon



sample_string = "vavascript"
new_string = "new"
len1 = len(sample_string)
print(len1)
half = int(len1/2)
print(half)

result = sample_string[:3] + new_string + sample_string[-3:]
print(result)