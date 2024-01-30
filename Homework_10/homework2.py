# Exercise 2:
# Write a Python program that asks the user to enter a password. Keep asking for the
# password until the correct password "secret" is entered. Provide appropriate feedback
# to the user.

#
password = input("Enter Password  >")
corrent_pass = "Secret"

while password != corrent_pass:
    password = input("Password is incorrect , Enter again > ")
if (password == corrent_pass):
    print(f"Your password is {password}")

