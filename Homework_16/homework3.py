# Write a python program that will raise an exception (Invalid
# File) if text file contents first symbol is starting with number
try:
    f = open("txt.txt", "r")
    if f is f.isdigit():
     raise print("first symbol is digit")
finally:
    print("jh")