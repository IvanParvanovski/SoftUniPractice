from collections import deque


def cups_and_bottles():
    cups = deque(map(int, input().split()))
    bottles = deque(map(int, input().split()))
    wasted_water = 0
    output = ""

    while cups and bottles:
        cup = cups.popleft()
        bottle = bottles.pop()
        if cup > bottle:
            cup -= bottle
            cups.appendleft(cup)
        else:
            wasted_water += bottle - cup
    if bottles:
        output = f"Bottles: {' '.join(map(str, bottles))}"
    elif cups:
        output = f"Cups: {' '.join(map(str, cups))}"

    output += f"\nWasted litters of water: {wasted_water}"
    print(output)


cups_and_bottles()