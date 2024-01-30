# 3.Smallest
# Write a Python program to get the smallest number from a list.

sample_list = [-15, 2, -5, -6]
small_digit = sample_list[0]
for from_list in sample_list:
    if from_list <= small_digit:
        small_digit = from_list
print(small_digit)
