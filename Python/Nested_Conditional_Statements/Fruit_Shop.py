fruit = input()
day = input()
count = float(input())

banana = 0
apple = 0
orange = 0
grapefruit = 0
kiwi = 0
pineapple = 0
grapes = 0
sum = 0


if day == "Saturday" or day == "Sunday":
    banana = 2.70
    apple = 1.25
    orange = 0.90
    grapefruit = 1.60
    kiwi = 3.00
    pineapple = 5.60
    grapes = 4.20

    if fruit == "banana":
        sum = banana * count
        print(f"{sum:.2f}")
    elif fruit == "apple":
        sum = apple * count
        print(f"{sum:.2f}")
    elif fruit == "orange":
        sum = orange * count
        print(f"{sum:.2f}")
    elif fruit == "grapefruit":
        sum = grapefruit * count
        print(f"{sum:.2f}")
    elif fruit == "kiwi":
        sum = kiwi * count
        print(f"{sum:.2f}")
    elif fruit == "pineapple":
        sum = pineapple * count
        print(f"{sum:.2f}")
    elif fruit == "grapes":
        sum = grapes * count
        print(f"{sum:.2f}")
    else:
        print("error")

elif day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":

    banana = 2.50
    apple = 1.20
    orange = 0.85
    grapefruit = 1.45
    kiwi = 2.70
    pineapple = 5.50
    grapes = 3.85

    if fruit == "banana":
        sum = banana * count
        print(f"{sum:.2f}")
    elif fruit == "apple":
        sum = apple * count
        print(f"{sum:.2f}")
    elif fruit == "orange":
        sum = orange * count
        print(f"{sum:.2f}")
    elif fruit == "grapefruit":
        sum = grapefruit * count
        print(f"{sum:.2f}")
    elif fruit == "kiwi":
        sum = kiwi * count
        print(f"{sum:.2f}")
    elif fruit == "pineapple":
        sum = pineapple * count
        print(f"{sum:.2f}")
    elif fruit == "grapes":
        sum = grapes * count
        print(f"{sum:.2f}")
    else:
        print("error")
else:
    print("error")
