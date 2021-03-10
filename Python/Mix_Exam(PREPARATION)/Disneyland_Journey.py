journey_costs = float(input())
months_count = int(input())
total_money = 0

for counter in range(1, months_count + 1):
    if counter % 4 == 0:
        total_money += 25 / 100 * total_money
    elif counter % 2 != 0 and counter != 1:
        total_money -= 16 / 100 * total_money

    total_money += 25 / 100 * journey_costs

output = ""
if total_money >= journey_costs:
    output = f"Bravo! You can go to Disneyland and you will have {total_money - journey_costs:.2f}lv. for souvenirs."
else:
    output = f"Sorry. You need {journey_costs - total_money:.2f}lv. more."

print(output)