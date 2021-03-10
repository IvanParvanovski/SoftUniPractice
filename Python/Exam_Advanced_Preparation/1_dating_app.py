from collections import deque

males = list(map(int, input().split()))
females = deque(map(int, input().split()))
matches = 0

while males and females:
    male_value = males.pop()
    female_value = females.popleft()

    if male_value <= 0 or female_value <= 0:
        if male_value <= 0 and female_value <= 0:
            continue

        elif male_value <= 0:
            females.appendleft(female_value)

        elif female_value <= 0:
            males.append(male_value)

    elif male_value % 25 == 0 or female_value % 25 == 0:
        if male_value % 25 == 0 and female_value % 25 == 0:
            males.pop()
            females.popleft()

        elif male_value % 25 == 0:
            males.pop()
            females.appendleft(female_value)

        elif female_value % 25 == 0:
            females.popleft()
            males.append(male_value)

    elif male_value == female_value:
        matches += 1

    else:
        males.append(male_value - 2)

# Males
males_output = ""
if males:
    males_output = ', '.join([str(x) for x in reversed(males)])
else:
    males_output = "none"

# Females
females_output = ""
if females:
    females_output = ', '.join([str(x) for x in females])
else:
    females_output = "none"

print(f"Matches: {matches}")
print(f"Males left: {males_output}")
print(f"Females left: {females_output}")
