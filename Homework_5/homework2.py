# 2.Largest
# Write a Python program to get the largest number from a list.
# Sample Input Sample Output
# [1, 2, 3, 4] 4
# [5, 7, 3, 9, 11] 11
# [25, 1,1, 13] 25
# [1, 2, 1, 1] 2


sample_list = [1, 2, 3, 4, 8]
largest_digit = sample_list[0]
for from_list in sample_list:
    if from_list >= largest_digit:
        largest_digit = from_list

print(largest_digit)


