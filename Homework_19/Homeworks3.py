# Given a list of numbers, write a function to find the sum of all numbers in the list that
# can be divided by 7.

def sum_of_divided_numbers(lst):
    sum_lst_numbers = 0
    for f in lst:
        if f % 7 == 0:
            sum_lst_numbers += f
    return sum_lst_numbers


print(sum_of_divided_numbers([99, 154, 5584, 7, 16, 66, 7]))