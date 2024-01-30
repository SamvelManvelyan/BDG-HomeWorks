# Write a Python program to add two given lists using map and
# lambda.(map-y kara function-ic heto mekic avel hajordakanutyun
# ynduni, orinak erku list)
# Original list:
# [1, 2, 3]
# [4, 5, 6]
# Result: after adding two list
# [5, 7, 9]

given_1 = [1, 2, 3]
given_2 = [4, 5, 6]
print(list(map(lambda c, o: c + o, given_1, given_2)))

