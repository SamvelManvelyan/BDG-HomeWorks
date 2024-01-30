# 7.Birth Year
# The program prompts the user their birth year. Assuming a person’s age
# is a non-negative integer not exceeding 120, output the user’s age or the
# words “Incorrect Year”. The sample outputs assume it’s currently the year
# 2016. If you are writing this program during any other year, the correct
# answers may differ. Store the value of the current year in a variable.
# Sample Input Sample Output
# 2016 0
# 2018 Incorrect Year
# 1903 113


current_year = 2023
sample_input1 = int(input("Enter your birthyear  "))
age = current_year - sample_input1
if sample_input1 >= current_year:
    print("Your age is  ", age)
elif age <= 120:
    print("Your age is  ", age)
else:
    print("Incorrect Year")
