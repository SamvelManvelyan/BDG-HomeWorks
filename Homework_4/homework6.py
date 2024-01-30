# 6.Comparison
# Input two positive integers, and output a line describing their relation.
# Follow the sample format.
# Sample Input Sample Output
# 7 9 7 < 9
# 11 11 11 = 11
# 4 -4 4 > -4

sample_input1 = int(input("Enter your first int  "))
sample_input2 = int(input("Enter your second int  "))
if sample_input1 == sample_input2:
    print(sample_input1, "=",  sample_input2)
elif sample_input1 > sample_input2:
    print(sample_input1, ">", sample_input2)
else:
    print(sample_input1, "<", sample_input2)