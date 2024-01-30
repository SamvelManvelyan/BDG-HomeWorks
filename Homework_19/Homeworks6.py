# 6. Tuple Exercise:
# Create a tuple of student names and their corresponding scores. Write a function to find
# the student with the highest score.

def highest_score(students):
    high_score = 1
    qayl = 1
    while qayl < len(students):
        score = students[qayl]
        if score > high_score:
            high_score = score
        qayl += 2
    return high_score


students = ("Samvel", 11, "Armen", 898, "Anna", 78, "Suren", 95, "Gurgen" , 261)
print(highest_score(students))
