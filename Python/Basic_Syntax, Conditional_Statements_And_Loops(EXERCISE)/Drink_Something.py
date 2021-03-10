input_age = int(input())

if input_age <= 14:
    print("drink toddy")
elif 14 < input_age <= 18:
    print("drink coke")
elif 18 < input_age <= 21:
    print("drink beer")
else:
    print("drink whisky")