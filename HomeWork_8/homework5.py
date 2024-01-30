# Exercise 5:
# You are given three lists, list1, list2, and list3. Your task is to implement a
# programm that takes these lists and prints the following:
# The set of elements that are common to all three lists.
# The set of elements that are unique to each list (present in only one list).


l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [3, 41, 5, 6, 77, 66]
l3 = [5, 6, 57, 8, 9 ,48]

common = set(l1) & set(l2) & set(l3)
unique1 = set(l1) - set(l2) - set(l3)
unique2 = set(l2) - set(l1) - set(l3)
unique3 = set(l3) - set(l1) - set(l2)

print("common", common)
print("unique 1 :", unique1)
print("unique 2:", unique2)
print("unique 3:", unique3)