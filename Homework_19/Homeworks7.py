# 7. Tuple Exercise:
# Write a function that swaps the values of two tuples.

def swap_tuples(t1, t2):
    change = t2 , t1
    return change


t1 = (123, "Samvel", ["Yerevan",555])
t2 = (425, "Anna", 54)

print(swap_tuples(t1, t2))