import  math

first_playerTime = int(input())
second_playerTime = int(input())
third_playerTime = int(input())

sum_of_times = first_playerTime + second_playerTime + third_playerTime

minutes = sum_of_times / 60
seconds = sum_of_times % 60

minutes = math.floor(minutes)

if seconds < 10:
    print(f"{minutes:.0f}:0{seconds:.0f}")
else:
    print(f"{minutes:.0f}:{seconds:.0f}")