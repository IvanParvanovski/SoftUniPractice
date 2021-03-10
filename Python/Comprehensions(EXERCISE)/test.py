bunker = {category: {} for category in input().split(", ")}
n = int(input())

for _ in range(n):
    tokens = input().split(" - ")
    category = tokens[0]
    item = tokens[1]
    quantity_and_quality = tokens[2].split(";")

    quantity = int(quantity_and_quality[0].split(":")[1])
    quality = int(quantity_and_quality[1].split(":")[1])
    bunker[category][item] = (quantity, quality)

count_items = sum([sum([x[0] for x in list(bunker[category].values())]) for category in bunker])
average_quality = sum([sum([x[1] for x in list(bunker[category].values())]) for category in bunker]) / len(bunker)

print(f"Count of items: {count_items}")
print(f"Average quality: {average_quality:.2f}")
[print(f"{category} -> {', '.join(bunker[category].keys())}") for category in bunker]
