from collections import deque


def crossroads(green_light_duration, free_window):
    cars = deque()
    raw_input = input()
    passed_cars_counter = 0

    while raw_input != "END":
        if raw_input != "green":
            cars.append(raw_input)
        else:
            window_light = free_window + green_light_duration
            while cars:
                if window_light - free_window > 0:
                    car = cars.popleft()
                    for char in car:
                        window_light -= 1
                        if window_light < 0:
                            return "A crash happened!" + f"\n{car} was hit at {char}."
                    passed_cars_counter += 1
                else:
                    break

        raw_input = input()
    return "Everyone is safe." + f"\n{passed_cars_counter} total cars passed the crossroads."


print(crossroads(int(input()), int(input())))
