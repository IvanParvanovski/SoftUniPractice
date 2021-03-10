def solve(operations_count, students_dict):
    create_student_dict(operations_count, students_dict)
    print_students_and_grades(students_dict)


def create_student_dict(count, students_dict):
    for _ in range(count):
        student_and_grade = input().split()
        student_name = student_and_grade[0]
        grade = student_and_grade[1]

        if student_name not in students_dict:
            students_dict[student_name] = list()
            students_dict[student_name].append(float(grade))
        else:
            students_dict[student_name].append(float(grade))


def print_students_and_grades(students_dict):
    for student in students_dict:
        each_student = students_dict[student]
        output = f"{student} -> "
        for each_grade in each_student:
            output += f"{each_grade:.2f} "
        print(output + f"(avg: {sum(each_student) / len(each_student):.2f})")


solve(int(input()), dict())