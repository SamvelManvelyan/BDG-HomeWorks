#Exercise 1: Counting Even Numbers

num = [1, 5, 65, 65, 112, 8, 6,]
even_count = 0
for x in num:
    if x % 2 == 0:
        even_count += 1
print("count of even numbers is" , even_count)
