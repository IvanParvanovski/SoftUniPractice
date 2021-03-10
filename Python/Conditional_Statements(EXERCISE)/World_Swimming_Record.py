from math import floor, ceil

record_in_seconds = float(input())
race_lenght = float(input())
time_for_1m = float(input())

lenght_of_attack = race_lenght / 15
floor_attack = floor(lenght_of_attack)
time_of_attack = floor_attack * 12.5


Ivan_time = race_lenght * time_for_1m + time_of_attack

deff = record_in_seconds - Ivan_time
deff = abs(deff)


if Ivan_time < record_in_seconds:
    print(f"Yes, he succeeded! The new world record is {Ivan_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {deff:.2f} seconds slower.")