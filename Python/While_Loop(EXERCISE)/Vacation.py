money_need_for_trip = float(input())
money_she_have = float(input())
total = money_she_have
days = 0
days_spended = 0


while total < money_need_for_trip:
    type_of_desicion = input()
    money_she_spend_or_save = float(input())
    days += 1

    if type_of_desicion == "save":
        total += money_she_spend_or_save
        days_spended = 0

    elif type_of_desicion == "spend":
        total -= money_she_spend_or_save
        days_spended += 1
        if total < 0:
            total = 0

    if days_spended >= 5:
        break
    elif total >= money_need_for_trip:
        break


if total >= money_need_for_trip and days_spended < 5:
    print(f"You saved the money for {days} days.")
else:
    print("You can't save the money.")
    print(f"{days}")