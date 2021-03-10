from collections import defaultdict
key_materials = {
    "shards": 0,
    "fragments": 0,
    "motes": 0
}

legendary_items = {
    "shards": "Shadowmourne",
    "fragments": "Valanyr",
    "motes": "Dragonwrath"
}


junks = defaultdict(int)
winner = ""

while winner == "":
    args = input().lower().split()

    for index in range(0, len(args), 2):
        quantity = int(args[index])
        material = args[index + 1]

        if material in key_materials:
            key_materials[material] += quantity

            if key_materials[material] >= 250:
                winner = material
                key_materials[material] -= 250
                break

        else:
            junks[material] += quantity

print(f"{legendary_items[winner]} obtained!")
sorted_key_materials = dict(sorted(key_materials.items(), key=lambda element: (-element[1], element[0])))
sorted_junks = dict(sorted(junks.items()))

for element in sorted_key_materials:
    print(f"{element}: {int(sorted_key_materials[element])}")

for element in sorted_junks:
    print(f"{element}: {int(sorted_junks[element])}")