def parking(cars_count):
    unique_cars = set()

    for _ in range(cars_count):
        (command, car_number) = input().split(', ')

        if command == "IN":
            unique_cars.add(car_number)
        elif command == "OUT":
            if car_number in unique_cars:
                unique_cars.remove(car_number)

    return unique_cars


raw_input = input()
if raw_input.isdigit():
    raw_input = int(raw_input)

    cars = parking(raw_input)
    if cars:
        for car in cars:
            print(car)
    else:
        print("Parking Lot is Empty")

else:
    print("Parking Lot is Empty")
