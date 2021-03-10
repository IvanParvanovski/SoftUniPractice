import math

money_FamilyGet = float(input())
grade = float(input())
minimum_salary = float(input())

#Social Stipendi
if money_FamilyGet < minimum_salary and 4.5 <= grade < 5.50:
    minimum_salary = 35 / 100 * minimum_salary
    floored_minimum_salary = math.floor(minimum_salary)
    print(f"You get a Social scholarship {minimum_salary} BGN")

#Excellent Results
if grade >= 5.5 and money_FamilyGet > minimum_salary:
    grade *= 25
    floored_grade = math.floor(grade)
    print(f"You get a scholarship for excellent results {floored_grade} BGN")

#No scholarship
if grade < 5.5 and money_FamilyGet > minimum_salary:
    print("You cannot get a scholarship!")


#Full
if money_FamilyGet < minimum_salary and grade >= 5.5:

    grade *= 25
    minimum_salary = 35 / 100 * minimum_salary
    floored_minimum_salary = math.floor(minimum_salary)
    floored_grade = math.floor(grade)

    if grade < minimum_salary:
        print(f"You get a Social scholarship {floored_minimum_salary} BGN")

    if minimum_salary < grade:
        print(f"You get a scholarship for excellent results {floored_grade} BGN")

    if floored_minimum_salary == floored_grade:
        print(f"You get a scholarship for excellent results {floored_grade} BGN")

