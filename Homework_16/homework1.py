# 1. Write a python program to read the whole text of a file and catch the error if files does not exists.


try:
    f = open("txt.txt", "r")
except FileNotFoundError as e:
    print(f"File is Missing {e}")
finally:
    print("End of Test")
