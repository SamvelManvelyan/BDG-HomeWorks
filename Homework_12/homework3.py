# Exercise 3: Average Function
# Write a function that calculates the average of a list of numbers.


def avarage_in_list_num(numbers):
    sum_of_elements = 0
    for i in numbers:
        sum_of_elements += i
    return sum_of_elements / len(numbers)


avarage_in_list_num([1, 51, 1, 1, 1])