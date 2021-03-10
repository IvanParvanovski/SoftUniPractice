people_on_wedding = int(input())
budget = int(input())

price_for_convert = people_on_wedding * 20

if price_for_convert < budget:
    left_money = budget - price_for_convert
    money_for_fireworks = 40 / 100 * left_money
    money_for_charity = left_money - money_for_fireworks
    print(f"Yes! {money_for_fireworks:.0f} lv are for fireworks and {money_for_charity:.0f} lv are for donation.")
else:
    money_needed = price_for_convert - budget
    print(f"They won't have enough money to pay the covert. They will need {money_needed:.0f} lv more.")