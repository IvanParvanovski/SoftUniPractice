from collections import deque
number_of_materials = list(map(int, input().split()))
magic_levels = deque(map(int, input().split()))

presents = {150: "Doll",
            250: "Wooden train",
            300: "Teddy bear",
            400: "Bicycle", }

crafted_presents = {"Doll": 0,
                    "Wooden train": 0,
                    "Teddy bear": 0,
                    "Bicycle": 0, }

while number_of_materials and magic_levels:
    material_value = number_of_materials.pop()
    magic_value = magic_levels.popleft()

    present_value = 0
    multiply_values = material_value * magic_value
    if multiply_values < 0:
        present_value = material_value + magic_value
        number_of_materials.append(present_value)

    else:
        if material_value == 0 or magic_value == 0:
            if material_value == 0 and magic_value == 0:
                continue

            elif material_value == 0:
                magic_levels.appendleft(magic_value)

            elif magic_value == 0:
                number_of_materials.append(material_value)

        elif multiply_values not in presents:
            present_value = material_value + 15
            number_of_materials.append(present_value)

        else:
            present_value = multiply_values
            crafted_presents[presents[present_value]] += 1

first_pair = True if crafted_presents["Doll"] >= 1 and crafted_presents["Wooden train"] >= 1 else False
second_pair = True if crafted_presents["Teddy bear"] >= 1 and crafted_presents["Bicycle"] >= 1 else False

if first_pair or second_pair:
    print("The presents are crafted! Merry Christmas!")

else:
    print("No presents this Christmas!")

if number_of_materials:
    print(f"Materials left: {', '.join(reversed([str(x) for x in number_of_materials]))}")

if magic_levels:
    print(f"Magic left: {', '.join([str(x) for x in magic_levels])}")

sorted_crafted_presents = sorted(crafted_presents)
for present in sorted_crafted_presents:
    if crafted_presents[present] > 0:
        print(f"{present}: {crafted_presents[present]}")
