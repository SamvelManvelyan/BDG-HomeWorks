# Exercise 2:
# Print a square pattern using a nested for loop. The pattern should have 5 rows and 5
# columns

# *  *  *  *  *
# *  *  *  *  *
# *  *  *  *  *
# *  *  *  *  *
# *  *  *  *  *


stars = ""
for x in range(5):
    for y in  range(1):
        if stars  < "*  *  *  *  *":
         stars += "*  *  *  *  *"
        print(stars)
