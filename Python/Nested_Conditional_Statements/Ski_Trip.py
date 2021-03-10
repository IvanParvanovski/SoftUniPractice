stayed_days = int(input())
stayed_days -= 1
room_type = input()
grade = input()

sum = 0

if stayed_days <= 10:
    room_for_one = 18.00
    apartment = 25.00
    president_apartment = 35.00

    if room_type == "room for one person":
        sum = room_for_one * stayed_days
    elif room_type == "apartment":
        sum = apartment * stayed_days
        sum -= 30 / 100 * sum
    elif room_type == "president apartment":
        sum = president_apartment * stayed_days
        sum -= 10 / 100 * sum

elif 10 < stayed_days <= 15:

    room_for_one = 18.00
    apartment = 25.00
    president_apartment = 35.00

    if room_type == "room for one person":
        sum = room_for_one * stayed_days
    elif room_type == "apartment":
        sum = apartment * stayed_days
        sum -= 35 / 100 * sum
    elif room_type == "president apartment":
        sum = president_apartment * stayed_days
        sum -= 15 / 100 * sum

elif stayed_days > 15:

    room_for_one = 18.00
    apartment = 25.00
    president_apartment = 35.00

    if room_type == "room for one person":
        sum = room_for_one * stayed_days
    elif room_type == "apartment":
        sum = apartment * stayed_days
        sum -= 50 / 100 * sum
    elif room_type == "president apartment":
        sum = president_apartment * stayed_days
        sum -= 20 / 100 * sum

if grade == "positive":
    sum += 25 / 100 * sum
elif grade == "negative":
    sum -= 10 / 100 * sum

print(f"{sum:.2f}")
