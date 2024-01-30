# 9. Dictionaries Exercise:
# Write a function that finds the key with the maximum value in a dictionary

def find_max():
    d1 = {"1": 30, "2": 66, "3": 199}
    convert = d1.values()
    l1 = []
    int1 = 0
    for x in convert:
        if x not in l1:
            l1.append(x)
    for z in l1:
        if z > int1:
            int1 = z
    return int1

print(find_max())

