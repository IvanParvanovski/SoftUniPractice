from collections import deque


def watter_que(water_quantity):
    raw_input = input()
    people_que = deque()

    while raw_input != "Start":
        people_que.append(raw_input)
        raw_input = input()

    while True:
        water_raw_input = input()

        if water_raw_input == "End":
            break

        elif water_raw_input.split()[0] == "refill":
            water_quantity += int(water_raw_input.split()[1])

        else:
            watter_dispenser = int(water_raw_input)
            if water_quantity - watter_dispenser >= 0:
                water_quantity -= watter_dispenser
                print(f"{people_que.popleft()} got water")
            else:
                print(f"{people_que.popleft()} must wait")

    return f"{water_quantity} liters left"


print(watter_que(int(input())))