import re
pattern = r"^[>]{2}(?P<item>[A-Za-z]+)[<]{2}(?P<number>\d+(\.\d+)*)[\!](?P<quantity>\d+)$"
total = 0
furniture = list()

command = input()
while command != "Purchase":
    all_valid_furniture = re.finditer(pattern, command)
    for element in all_valid_furniture:
        furniture.append(element.group("item"))
        total += float(element.group("number")) * int(element.group("quantity"))
    command = input()

print("Bought furniture:")

for element in furniture:
    print(element)

print(f"Total money spend: {total:.2f}")