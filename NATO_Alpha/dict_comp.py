import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie" ]

students_score = {student:random.randint(1, 100) for student in names }

passed_students = {student:value for student, value in students_score.items() if value >= 60 }
print(students_score)
print(passed_students)