first_employee_efficiency = int(input()) # 1
second_employee_efficiency = int(input()) # 2
third_employee_efficiency = int(input()) # 3
answered_question_per_hour = first_employee_efficiency + second_employee_efficiency + third_employee_efficiency # 6
people_count = int(input()) # 45
hour = 0
while people_count > 0:
    answered_people = 0
    hour += 1
    if hour % 4 != 0:
        answered_people += answered_question_per_hour
        if people_count < answered_people:
            answered_people = people_count
        people_count -= answered_people
print(f"Time needed: {hour}h.")

