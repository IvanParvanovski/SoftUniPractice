degrees = int(input())
time_of_the_day = input()
outfit = ""
shoes = ""

if 10 <= degrees <= 18:
    if time_of_the_day == "Morning":
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif time_of_the_day == "Afternoon":
        outfit = "Shirt"
        shoes = "Moccasins"
    elif time_of_the_day == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"

elif 18 < degrees <= 24:
    if time_of_the_day == "Morning":
        outfit = "Shirt"
        shoes = "Moccasins"
    elif time_of_the_day == "Afternoon":
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif time_of_the_day == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"

elif degrees >= 25:
    if time_of_the_day == "Morning":
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif time_of_the_day == "Afternoon":
        outfit = "Swim Suit"
        shoes = "Barefoot"
    elif time_of_the_day == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"

print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
