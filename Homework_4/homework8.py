# 8.Three Numbers
# Input three integers. Output the word “Sorted” if the numbers are listed in
# a non-increasing or non-decreasing order and “Unsorted” otherwise.
# Sample Input Sample Output
# 1 2 3 Sorted
# 1 3 2 Unsorted
# 5 0 -4 Sorted
# 9 9 9 Sorted
# 9 9 0 Sorted


sample_imput1 = int(input("Enter your first int "))
sample_imput2 = int(input("Enter your second int "))
sample_imput3 = int(input("Enter your third int "))

if sample_imput1 <= sample_imput2 <= sample_imput3:
    print("Sorted")
elif sample_imput1 >= sample_imput2 >= sample_imput3:
    print("Sorted")
else:
    print("Unsorted")
