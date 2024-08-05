student_heights = input("Enter a list of students heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int (student_heights[n])
print(student_heights) 

total_heights = 0
for height in student_heights:
    total_heights += height
print(total_heights)

students_number = 0
for student in student_heights:
    students_number += 1
print(students_number)

average_height = round(total_heights / students_number)
print(average_height)