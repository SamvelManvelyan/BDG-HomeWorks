# 4. Write a Python program to find intersection of two given arrays using
# Lambda.
# Original arrays:
# [1, 2, 3, 5, 7, 8, 9, 10]
# [1, 2, 4, 8, 9]


#Seov

given1 = [1, 2, 3, 5, 7, 8, 9, 10]
given2 = [1, 2, 4, 8, 9]
print(list(filter(lambda o: o in given1, given2)))



