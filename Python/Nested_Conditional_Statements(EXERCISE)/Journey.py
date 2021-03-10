budget = float(input())
season = input()
holiday_house = ""
sum = 0
place = ""

if season == "summer":
    holiday_house = "Camp"

    if budget <= 100:
        sum = budget - 30 / 100 * budget
        place = "Bulgaria"
    elif 100 < budget <= 1000:
        sum = budget - 40 / 100 * budget
        place = "Balkans"
    elif 1000 < budget:
        holiday_house = "Hotel"
        sum = budget - 90 / 100 * budget
        place = "Europe"
    budget = budget - sum

    print(f"Somewhere in {place}")
    print(f"{holiday_house} - {budget:.2f}")

if season == "winter":
    holiday_house = "Hotel"

    if budget <= 100:
        sum = budget - 70 / 100 * budget
        place = "Bulgaria"
    elif 100 < budget <= 1000:
        sum = budget - 80 / 100 * budget
        place = "Balkans"
    elif 1000 < budget:
        sum = budget -  90 / 100 * budget
        place = "Europe"
    budget = budget - sum

    print(f"Somewhere in {place}")
    print(f"{holiday_house} - {budget:.2f}")


