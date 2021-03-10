student_name = input()
grades_count = 1
total = 0

while grades_count <= 12:
    grade = float(input())

    if grade >= 4:
        total += grade
        grades_count += 1

average_grade = total / 12


print(f"{student_name} graduated. Average grade: {average_grade:.2f}")