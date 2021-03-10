bad_grades_FAIL_TIME = int(input())
bad_grades_counter = 0
total = 0
grade_counter = 1
problem_counter = 1

exercise_name = input()
grade = int(input())
last_exercise = ""

while exercise_name != "Enough" or bad_grades_counter >= bad_grades_FAIL_TIME:
    total += grade

    if grade <= 4.00:
        bad_grades_counter += 1

    if bad_grades_counter >= bad_grades_FAIL_TIME:
        break

    last_exercise = exercise_name
    exercise_name = input()
    if exercise_name == "Enough":
        break
    grade = int(input())
    grade_counter += 1
    problem_counter += 1

average_score = total / grade_counter

if exercise_name == "Enough":
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {problem_counter}")
    print(f"Last problem: {last_exercise}")

else:
    print(f"You need a break, {bad_grades_counter} poor grades.")
