names = input().split(', ')
heroes_dict = {name: list() for name in names}
while True:
    raw_input = input().split('-')
    if raw_input[0] == "End":
        break

    hero_name = raw_input[0]
    item = raw_input[1]
    item_price = raw_input[2]

    if item not in heroes_dict[hero_name]:
        heroes_dict[hero_name].append(item)
        heroes_dict[hero_name].append(int(item_price))

[print(f"{name} -> Items: {int(len(heroes_dict[name]) / 2)}, Cost: {sum([heroes_dict[name][index]for index in range(1, len(heroes_dict[name]), 2)])}") for name in heroes_dict]