from collections import deque


def are_secondary_colors_valid(colors):
    if "orange" in colors:
        if "red" not in colors or "yellow" not in colors:
            colors.remove("orange")

    if "purple" in colors:
        if "red" not in colors or "blue" not in colors:
            colors.remove("purple")

    if "green" in colors:
        if "yellow" not in colors or "blue" not in colors:
            colors.remove("green")

    return colors


main_colors = {"red",
               "yellow",
               "blue", }

secondary_colors = {"orange",
                    "purple",
                    "green", }

crafted_colors = list()
colors = deque(input().split())

while colors:
    first_part = colors.popleft()
    second_part = colors.pop() if colors else ""
    first_match = first_part + second_part
    second_match = second_part + first_part

    if first_match in main_colors or first_match in secondary_colors:
        crafted_colors.append(first_match)
    elif second_match in main_colors or second_match in secondary_colors:
        crafted_colors.append(second_match)
    else:
        if len(first_part) > 1:
            colors.insert(len(colors) // 2, first_part[:-1:])

        if len(second_part) > 1:
            colors.insert(len(colors) // 2, second_part[:-1:])


crafted_colors = are_secondary_colors_valid(crafted_colors)
print(crafted_colors)
