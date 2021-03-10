budget = int(input())
decoration_type = ""
left_sum = 0
total = 0

while decoration_type != "Stop":
    total = 0
    decoration_type = input()
    if decoration_type == "Stop":
        break
    decoration_type_lenght = len(decoration_type)

    for index in range(decoration_type_lenght):
        total += ord(decoration_type[index])

    if budget >= total:
        print("Item successfully purchased!")
    else:
        print("Not enough money!")
        break

    budget -= total
if budget > total:
    diff = budget - total
    print(f"Money left: {diff}")