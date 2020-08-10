number = int(input())

students = {}

for i in range(number):
    student_name = input()
    student_grade = float(input())

    if student_name not in students:
        students[student_name] = []

    students[student_name].append(student_grade)

student_avg_grades = {}

for student, grades in students.items():
    avg = sum(grades) / len(grades)
    if avg < 4.5:
        continue
    student_avg_grades[student] = avg

student_avg_grades = dict(sorted(student_avg_grades.items(), key=lambda c: c[1], reverse=True))

for student, avrg in student_avg_grades.items():
    print(f"{student} -> {avrg:.2f}")