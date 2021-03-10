needed_experience = float(input())
battles_count = int(input())
total = 0
output = ""

for counter in range(1, battles_count + 1):
    experience = float(input())
    if counter % 3 == 0:
        experience += 15 / 100 * experience
    elif counter % 5 == 0:
        experience -= 10 / 100 * experience

    total += experience
    if total >= needed_experience:
        output = f"Player successfully collected his needed experience for {counter} battles."
        break
    else:
        output = f"Player was not able to collect the needed experience, {needed_experience - total:.2f} more needed."
print(output)