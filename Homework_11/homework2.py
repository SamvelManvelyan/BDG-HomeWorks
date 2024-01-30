# 2.Letters Count
# Write a Python function to calculate count of each letter in string
# Sample Input Sample Output
# count_letters(‘abrakadabra’)
# {a: 5, b: 2, r: 2, k: 1, d: 1}


def count_of_latters(word):
    datark_dict = {}
    for x in word:
        if x not in datark_dict:
            datark_dict = x
        elif x in datark_dict:
            datark_dict +=1
    return datark_dict

count_of_latters("abrakadabra")

dict = {"key": 10}

