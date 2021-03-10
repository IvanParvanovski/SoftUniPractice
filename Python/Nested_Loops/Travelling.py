destination = input()

while destination != "End":
    minBudget = float(input())
    total = 0

    while total < minBudget:
        total += float(input())

    print(f"Going to {destination}!")

    total = 0
    destination = input()