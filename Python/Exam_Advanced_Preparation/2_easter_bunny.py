import sys

def create_field(size):
    matrix = list()
    for _ in range(size):
        matrix.append(input().split())
    return matrix


def find_rabbit(matrix):
    for index in range(len(matrix)):
        row = matrix[index]
        if "B" in row:
            return index, row.index("B")


field_size = int(input())
field = create_field(field_size)
rabbit_position = find_rabbit(field)

direction_increases = {"up": (-1, 0),
                       "down": (1, 0),
                       "right": (0, 1),
                       "left": (0, -1), }

directions_positions = {"up": [],
                        "down": [],
                        "right": [],
                        "left": [], }

highest_sum = -sys.maxsize
best_direction = ""
for direction in direction_increases:
    current_sum = 0
    rabbit_row = rabbit_position[0]
    rabbit_col = rabbit_position[1]
    gone_threw = False

    if direction == "up":
        while rabbit_row > 0:
            rabbit_row += direction_increases[direction][0]
            token = field[rabbit_row][rabbit_col]
            if token.isdigit():
                gone_threw = True
                current_sum += int(token)
                directions_positions[direction].append([rabbit_row, rabbit_col])
            else:
                break

    elif direction == "down":
        while rabbit_row < len(field) - 1:
            rabbit_row += direction_increases[direction][0]
            token = field[rabbit_row][rabbit_col]
            if token.isdigit():
                gone_threw = True
                current_sum += int(token)
                directions_positions[direction].append([rabbit_row, rabbit_col])
            else:
                break

    elif direction == "right":
        while rabbit_col < len(field) - 1:
            rabbit_col += direction_increases[direction][1]
            token = field[rabbit_row][rabbit_col]
            if token.isdigit():
                current_sum += int(token)
                gone_threw = True
                directions_positions[direction].append([rabbit_row, rabbit_col])
            else:
                break

    elif direction == "left":
        while rabbit_col > 0:
            rabbit_col += direction_increases[direction][1]
            token = field[rabbit_row][rabbit_col]
            if token.isdigit():
                current_sum += int(token)
                gone_threw = True
                directions_positions[direction].append([rabbit_row, rabbit_col])
            else:
                break

    if current_sum > highest_sum and gone_threw:
        highest_sum = current_sum
        best_direction = direction

print(best_direction)
[print(x) for x in directions_positions[best_direction]]
print(highest_sum)
