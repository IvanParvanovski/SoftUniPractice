student_name = input()
total = 0
grade_counter = 1
times_failed = 0


while grade_counter <= 12:
    grade = float(input())

    if grade < 4.00:
        times_failed += 1

        if times_failed >= 2:
            grade_counter -= 1
            break

        grade_counter += 1
        total += grade_counter

    else:
        grade_counter += 1
        total += grade

if times_failed >= 2:
    print(f"{student_name} has been excluded at {grade_counter} grade")

else:
    average_grade = total / 12
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")