import math

exam_hour_time = int(input())
exam_minute_time = int(input())
user_hour_time = int(input())
user_minute_time = int(input())

set = False

exam_time = exam_hour_time * 60 + exam_minute_time
user_time = user_hour_time * 60 + user_minute_time

diff = exam_time - user_time

hours = diff // 60
minutes = diff % 60

if diff < 0 and set == False:
    print("Late")
    diff = abs(diff)
    if diff >= 60:
        hours = diff // 60
        minutes = diff % 60
        print("{}:{:02d} hours after the start".format(hours, minutes))
    else:
        print(f"{diff} minutes after the start")

    set = True

if diff > 30 and set == False:
    print("Early")

    if hours < 1 and minutes > 0:
        print(f"{minutes:.0f} minutes before the start")

    elif hours >= 1 and minutes > 10:
        print(f"{hours:.0f}:{minutes:.0f} hours before the start ")

    elif hours >= 1 and minutes < 10:
        print(f"{hours:.0f}:0{minutes:.0f} hours before the start")

    set = True

if 0 <= diff <= 30 and set == False:
    diff = abs(diff)
    print("On time")

    if hours < 1 and minutes > 0:
        print(f"{minutes} minutes before the start")

    elif hours >= 1 and minutes > 10:
        print(f"{hours:.0f}:{minutes} hours before the start")

    elif hours >= 1 and minutes < 10:
        print(f"{hours:.0f}:{minutes} hours before the start")

    set = True
