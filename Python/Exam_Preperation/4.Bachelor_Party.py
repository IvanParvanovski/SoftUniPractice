singer_sum = int(input())
people_count = input()
counter = 0
total = 0

while people_count != "The restaurant is full":
    people_count = int(people_count)
    if people_count < 5:
        total += 100 * people_count
    elif people_count >= 5:
        total += 70 * people_count
    counter += int(people_count)
    people_count = input()

if total >= singer_sum:
    diff = total - singer_sum
    print(f"You have {counter} guests and {diff} leva left.")
else:
    print(f"You have {counter} guests and {total} leva income, but no singer.")