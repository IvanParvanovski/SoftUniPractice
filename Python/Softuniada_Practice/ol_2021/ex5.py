from collections import deque

employees = list(int(x) for x in input().split(', '))
sorted_employees = deque(sorted(employees))
packages_count = int(input())
candies_per_bag = sum(employees) // packages_count

while employees:
    main_num = sorted_employees.pop()
    current_package = [main_num]

    while sum(current_package) < candies_per_bag:
        current_num = sorted_employees.popleft()
        following_num = sorted_employees.popleft()
        if sum(current_package)
        current_package.append()

    print(current_package)