# 5. Math Operations Exercise:
# Write a function that calculates the square root of a number using the math module.

import math


def calculate_square_root(number):
    if number < 0:
        return "Xndrum enq mutqagrel drakan tiv"
    else:
        result = math.sqrt(number)
        return result


print(calculate_square_root(4))