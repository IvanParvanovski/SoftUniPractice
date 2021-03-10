item = input()
city = input()
count = float(input())
water = 0
coffee = 0
beer = 0
sweets = 0
peanuts = 0
sum = 0

if city == "Sofia":
    water = 0.80
    coffee = 0.50
    beer = 1.20
    sweets = 1.45
    peanuts = 1.60

    if item == "water":
        sum = water * count
    if item == "coffee":
        sum = coffee * count
    if item == "beer":
        sum = beer * count
    if item == "sweets":
        sum = sweets * count
    if item == "peanuts":
        sum = peanuts * count

if city == "Plovdiv":
    water = 0.70
    coffee = 0.40
    beer = 1.15
    sweets = 1.30
    peanuts = 1.50

    if item == "water":
        sum = water * count
    if item == "coffee":
        sum = coffee * count
    if item == "beer":
        sum = beer * count
    if item == "sweets":
        sum = sweets * count
    if item == "peanuts":
        sum = peanuts * count

if city == "Varna":
    water = 0.70
    coffee = 0.45
    beer = 1.10
    sweets = 1.35
    peanuts = 1.55

    if item == "water":
        sum = water * count
    if item == "coffee":
        sum = coffee * count
    if item == "beer":
        sum = beer * count
    if item == "sweets":
        sum = sweets * count
    if item == "peanuts":
        sum = peanuts * count

print(sum)
