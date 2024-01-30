# 1.Multiply
# Write a Python program to multiply all the items in a list.
# Sample Input Sample Output
# [1, 2, 3, 4] 24
# [5, 7, 3, 9, 11] 10395
# [25, 1,1, 13] 325

sample_list = [5, 7, 3, 9, 11]
multi = 1
for from_list in sample_list:
    multi = multi * from_list
print(multi)
