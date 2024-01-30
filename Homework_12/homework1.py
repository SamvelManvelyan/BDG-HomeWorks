# Exercise 1: Check Pangram Function
# Write a function that checks if a sentence is a pangram


def word_is_pangram(word):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    for x in alphabet:
        if x not in word:
            return False

    return True


print(word_is_pangram('abcdefghijklmnopqrstuvwxyz'))