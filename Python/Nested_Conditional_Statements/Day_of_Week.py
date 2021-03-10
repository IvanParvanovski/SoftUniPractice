num = int(input())
day = ""

if num <= 7:
    if num == 1:
        day = "Monday"
    if num == 2:
        day = "Tuesday"
    if num == 3:
        day = "Wednesday"
    if num == 4:
        day = "Thursday"
    if num == 5:
        day = "Friday"
    if num == 6:
        day = "Saturday"
    if num == 7:
        day = "Sunday"
    print(day)
else:
    day = "Error"
    print(day)
