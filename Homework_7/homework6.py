# 4)Count how many uppercase and lowercase characters are in this sentence.(“The Quick
# Brown Fox”)

word = "The Quick Brown Fox"
upper = []
lower = []
for x in word:
    if  x.isupper():
        upper.append(x)
    else:
        lower.append(x)

print("In word ", len(upper), "is upper and", len(lower), "is lower latters" )