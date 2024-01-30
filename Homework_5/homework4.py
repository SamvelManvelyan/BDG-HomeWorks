# 4.Second smallest
# Write a Python program to find the second smallest number in a list.
# Sample Input Sample Output
# [1, 2, 3, 4] 2
# [5, 7, 3, 9, 11] 5
# [25, 1,1, 13] 1


cucak = [5, 7, 3, 9, 11, 95, 4]
first_small_number = cucak[0]
second_small_number = cucak[0]
for qayl in cucak:
    if qayl < first_small_number:
        second_small_number = first_small_number
        first_small_number = qayl
    elif  qayl >second_small_number and second_small_number <= first_small_number:
            second_small_number = qayl
    elif qayl <second_small_number and second_small_number >= first_small_number:
        second_small_number = qayl

print(second_small_number)



