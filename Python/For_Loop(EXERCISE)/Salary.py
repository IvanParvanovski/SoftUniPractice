web_sites_opened = int(input())
employee_salary = int(input())

for counter in range(web_sites_opened):

    if employee_salary > 0:
        web_sites = input()

        if web_sites.lower() == "facebook":
            employee_salary -= 150
        if web_sites.lower() == "instagram":
            employee_salary -= 100
        if web_sites.lower() == "reddit":
            employee_salary -= 50

if employee_salary <= 0:
    print("You have lost your salary.")
else:
    print(employee_salary)