days_of_vacation = int(input()) # 7
budget = float(input()) # 12000
people_count = int(input()) # 5
fuel_per_kilometer = float(input()) # 1.5
food_expenses_per_person = float(input()) # 10
room_price_per_night = float(input()) # 20

discount = 0
output = ""

hotel_expenses = room_price_per_night * people_count * days_of_vacation # 700
food_expenses = food_expenses_per_person * people_count * days_of_vacation # 350

if people_count > 10:
    discount = 25 / 100 * hotel_expenses

expenses = hotel_expenses + food_expenses

for day in range(1, days_of_vacation + 1):
    kilometers = float(input())
    travel_expenses = kilometers * fuel_per_kilometer

    if expenses > budget:
        output = f"Not enough money to continue the trip. You need {expenses - budget:.2f}"
        break
    else:
        expenses += travel_expenses # 8645.652

        if day % 3 == 0 or day % 5 == 0:
            expenses += 40 / 100 * expenses

        elif day % 7 == 0:
            expenses -= expenses / people_count

        output = f"You have reached the destination. You have {budget - expenses:.2f}$ budget left"

print(output)