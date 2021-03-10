companies_with_employees = dict()
args = input()
while args != "End":
    args = args.split(" -> ")
    company_name = args[0]
    employee_id = args[1]
    if company_name not in companies_with_employees:
        companies_with_employees[company_name] = list()
    if employee_id not in companies_with_employees[company_name]:
        companies_with_employees[company_name].append(employee_id)
    args = input()

reversed_companies_with_employees = sorted(companies_with_employees)
for company in reversed_companies_with_employees:
    print(company)
    for employee_id in companies_with_employees[company]:
        print(f"-- {employee_id}")