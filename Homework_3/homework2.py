# 2. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If
# the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string
# is less than 3, leave it unchanged.
# Example:
# Sample String : 'abc'
# Expected Result : 'abcing'
# _______________________
# Sample String : 'string'
# Expected Result : 'stringly'


sample1 = 'abc'
if len(sample1)  >= 3 :
    print(sample1 + "ing")
else:
    print(sample1)

simple2 = 'string'
if len(simple2) > 3:
    print(simple2 + 'ly' )
else:
    print(simple2)






