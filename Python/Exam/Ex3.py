power = int(input())
city = input()
standart = input()
total = 0

if city == "Sofia":
    if power <= 37:
        total = 1.43 * power
    elif 38 <= power <= 55:
        total = 1.50 * power
    elif power >= 55:
        total = 2.68 * power
elif city == "Vidin":
    if power <= 37:
        total = 1.34 * power
    elif 38 <= power <= 55:
        total = 1.40 * power
    elif power >= 55:
        total = 2.54 * power
elif city == "Varna":
    if power <= 37:
        total = 1.37 * power
    elif 38 <= power <= 55:
        total = 1.40 * power
    elif power >= 55:
        total = 2.57 * power


if standart == "Euro 4":
    total -= 15 / 100 * total
elif standart == "Euro 5":
    total -= 17 / 100 * total
elif standart == "Euro 6":
    total -= 20 / 100 * total

print(f"{total:.2f} lv")