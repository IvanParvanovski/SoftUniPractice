hours = int(input())
minutes = int(input())

minutes += 15


if minutes > 59:
    hours += 1
    minutes %= 60

if hours < 24 and minutes >= 10:
    print(f"{hours}:{minutes}")
if hours < 24 and minutes <= 9:
    print(f"{hours}:0{minutes}")
if hours == 24 and minutes <= 9:
    print(f"0:0{minutes}")
if hours == 24 and minutes >= 10:
    print(f"0:{minutes}")
