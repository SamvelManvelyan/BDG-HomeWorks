# Exercise 4:
# Write a Python program that generates a random number between 1 and 100 and asks
# the user to guess the number. The program should give hints whether the guessed
# number is too high or too low until the correct number is guessed.

import random
random_number = random.randint(1, 100)

your = int(input("Enter Numb > "))
while your != random_number:
    if your < random_number:
        your = int(input("your numb is  low Enter Numb again > "))
    elif your > random_number:
        your = int(input("your numb is  large Enter Numb again > "))
if your == random_number:
        print(f"Uraa corrent numb is {random_number}")



