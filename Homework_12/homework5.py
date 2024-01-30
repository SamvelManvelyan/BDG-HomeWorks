# Exercise 5: Sum of Squares Function
# Write a function that calculates the sum of squares of numbers from 1 to n

def sum_of_squares(number):
    sum = 0
    for x in range(1, number+1):
        sum += x*x
    return sum

print(sum_of_squares(100))

