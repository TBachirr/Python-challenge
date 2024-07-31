students_scores= {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
    }
students_grades = {}
for student in students_scores:
    if students_scores[student] > 90:
        students_grades[student] = "Outstanding"
    elif students_scores[student] > 80:
        students_grades[student] = "Exceeds Expectations"
    elif students_scores[student] > 70:
        students_grades[student] = "Acceptable"
    else:
        students_grades[student] = "Fail"