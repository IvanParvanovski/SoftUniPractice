judges = int(input())
presentation_name = input()
total = 0
judges_counter = 0

while presentation_name != "Finish":
    presentation_total = 0
    for counter in range(judges):
        grade = float(input())
        presentation_total += grade
        total += grade
        judges_counter += 1

    presentation_average = presentation_total / judges

    print(f"{presentation_name} - {presentation_average:.2f}.")
    presentation_name = input()

average = total / judges_counter
print(f"Student's final assessment is {average:.2f}.")


