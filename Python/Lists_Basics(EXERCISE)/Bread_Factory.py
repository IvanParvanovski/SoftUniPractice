all_events = input().split("|")
energy = 100
coins = 100
isClosed = False

for index in range(len(all_events)):
    each_element_in_events = all_events[index].split("-")
    event = each_element_in_events[0]
    num = int(each_element_in_events[1])

    if event == "rest":
        if energy < 100:
            energy += num

            if energy > 100:
                num = 0
                energy = 100
        else:
            num = 0
        print(f"You gained {num} energy.")
        print(f"Current energy: {energy}.")

    elif event == "order":
        energy -= 30
        if energy > 0:
            coins += num
            print(f"You earned {num} coins.")
        else:
            energy += 80

            if energy > 100:
                energy = 100

            print(f"You had to rest!")

    else:
        coins -= num
        if coins > 0:
            print(f"You bought {event}.")
        else:
            print(f"Closed! Cannot afford {event}.")
            isClosed = True
            break

if isClosed is not True:
    print(f"Day completed!\nCoins: {coins}\nEnergy: {energy}")
