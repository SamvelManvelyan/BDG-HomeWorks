# 2)Write a Python script that takes a list of words and return the longest word and the
# length of the longest one.

word = ["Gyumri", "ijevan", "spitak", "kapan", "Yerevan"]
long_check = word[0]
long_word = []
for x in word:
    if len(long_check) <= len(x):
        long_word = x
print("The long word is:" ,long_word , "Leght is " , len(long_word) )

