rows_pair = int(input())
students_grades = dict()
student_average_grade = dict()

for _ in range(rows_pair):
    student_name = input()
    grade = float(input())

    if student_name not in students_grades:
        students_grades[student_name] = list()
    students_grades[student_name].append(float(grade))

for student, grades in students_grades.items():
    average_grade = sum(grades) / len(grades)
    student_average_grade[student] = average_grade


sorted_student_average_grade = sorted(student_average_grade.items(), key=lambda element: element[1], reverse=True)

for student, average_grade in sorted_student_average_grade:
    if average_grade >= 4.50:
        print(f"{student} -> {average_grade:.2f}")