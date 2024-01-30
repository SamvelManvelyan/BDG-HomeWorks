# 6. Write a Python function to get a string made of its first three characters of a specified string. If
# the length of the string is less than 3 then return the original string.
# Example:
# Sample ='ipy'
# Expected ipy
# ______________
# Sample ='python'
# Expected pyt


# with function
def get_first_three_chars(sample):
    if len(sample) < 3:
        return sample
    else:
        return sample[:3]

sample1 = 'ipy'
result1 = get_first_three_chars(sample1)

sample2 = 'python'
result2 = get_first_three_chars(sample2)


