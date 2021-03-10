group_money = int(input())
season = input()
people = int(input())
sum = 0
deff = 0

if season == "Spring":
    sum = 3000

    if people % 2 == 0:
        sum -= 5 / 100 * sum

if season == "Summer":
    sum = 4200

    if people % 2 == 0:
        sum -= 5 / 100 * sum

if season == "Autumn":
    sum = 4200

if season == "Winter":
    sum = 2600

    if people % 2 == 0:
        sum -= 5 / 100 * sum

if people <= 6:
    sum -= 10 / 100 * sum
elif 7 <= people <= 11:
        sum -= 15 / 100 * sum
elif people >= 12:
    sum -= 25 / 100 * sum

if group_money >= sum:
    deff = group_money - sum
    print(f"Yes! You have {deff:.2f} leva left.")
elif sum > group_money:
    deff = sum - group_money
    print(f"Not enough money! You need {deff:.2f} leva.")
