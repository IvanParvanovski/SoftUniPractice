from collections import defaultdict
course_class = defaultdict(list)
course_people = defaultdict(int)
args = input()

while args != "end":
    args = args.split(" : ")
    course = args[0]
    student_name = args[1]

    course_class[course].append(student_name)
    course_people[course] += 1

    args = input()

sorted_course_class = sorted(course_class, key=lambda element: -course_people[element])

for course in sorted_course_class:
    print(f"{course}: {course_people[course]}")
    sorted_course_people = sorted(course_class[course])

    for person in sorted_course_people:
        print(f"-- {person}")
