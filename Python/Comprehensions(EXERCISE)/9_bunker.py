categories = {element: list() for element in input().split(', ')}
quantity = 0
quality = 0
lines_count = int(input())
for _ in range(lines_count):
    raw_input = input().split(" - ")

    category = raw_input[0]
    item = raw_input[1]
    quantity_and_quality = [(element.split(':')[0], element.split(':')[1]) for element in raw_input[2].split(';')]

    quantity += int(quantity_and_quality[0][1])
    quality += int(quantity_and_quality[1][1])

    categories[category].append(item)

print(f"Count of items: {quantity}")
print(f"Average quality: {quality / len(categories):.2f}")
[print(f"{category} -> {', '.join(items_list)}") for category, items_list in categories.items()]
