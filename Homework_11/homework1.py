# 1.Max of Three
# Write a Python function to find the Max of three numbers.
# Sample Input Sample Output
# max_of_three(5, 11, 3)
# 11


def max_of_numbers(a,b,c):
    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    else:
        print(c)

max_of_numbers(5, 11, 3)