flower = input()
count = int(input())
family_money = int(input())
sum = 0

deff = 0

# Flowers price
rose = 5
dahlia = 3.80
tulip = 2.80
daffodil = 3
gladiola = 2.50

if flower == "Roses":
    sum = rose * count
    if count > 80:
        sum -= 10 / 100 * sum

elif flower == "Dahlias":
    sum = dahlia * count
    if count > 90:
        sum -= 15 / 100 * sum

elif flower == "Tulips":
    sum = tulip * count
    if count > 80:
        sum -= 15 / 100 * sum

elif flower == "Narcissus":
    if count < 120:
        sum = daffodil * count
        sum += 15 / 100 * sum
    else:
        sum = daffodil * count

elif flower == "Gladiolus":
    if count < 80:
        sum = gladiola * count
        sum += 20 / 100 * sum
    else:
        sum = gladiola * count


if family_money >= sum:
    deff = family_money - sum
    print(f"Hey, you have a great garden with {count} {flower} and {deff:.2f} leva left.")
else:
    deff = sum - family_money
    print(f"Not enough money, you need {deff:.2f} leva more.")
