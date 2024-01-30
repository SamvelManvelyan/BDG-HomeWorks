# 5.Duplicates
# Write a Python program to remove duplicates from a list.
# Sample Input Sample Output
# [1, 2, 3, 1] [1, 2, 3]
# [5, 7, 3, 9, 11] [5, 7, 3, 9, 11]
# [25, 1,1, 13] [25, 1, 13]

sample_list = [25, 1,1, 13]
datark_list = []
for looking in sample_list:
    if looking not in datark_list:
        datark_list.append(looking)
        sample_list = datark_list

print(sample_list)
