# Write a function that takes two lists and returns a new list containing only the common
# elements. (without using set)

def common_elements():
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 6, 7]
    result = []
    for f in list1:
       if f in list2:
        result.append(f)
    return result


print(common_elements())
