students_score = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

students_grades = {}

for student in students_score:
    score = students_score[student]
    if score > 90:
        students_grades[student] = "Outstanding"
    elif score > 80:
        students_grades[student] = "Exceed Expectations"
    elif score > 70:
        students_grades[student] = "Acceptable"
    else:
        students_grades[student] = "Fail"
        
print(students_grades)