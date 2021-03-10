def drop_presents(pos, matrix, available_presents):
    row = pos[0]
    col = pos[1]
    result = 0

    if matrix[row][col - 1] in "XV" and available_presents > 0:
        result += 1
        matrix[row][col - 1] = "-"
        available_presents -= 1

    if matrix[row][col + 1] in "XV" and available_presents > 0:
        result += 1
        matrix[row][col + 1] = "-"
        available_presents -= 1

    if matrix[row - 1][col] in "XV" and available_presents > 0:
        result += 1
        matrix[row - 1][col] = "-"
        available_presents -= 1

    if matrix[row + 1][col] in "XV" and available_presents > 0:
        result += 1
        matrix[row + 1][col] = "-"
        available_presents -= 1

    return result


def get_nice_kids(matrix):
    result = 0
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == "V":
                result += 1
    return result


presents = int(input())
n = int(input())
santa_pos = []

matrix = []
directions = {"up": (-1, 0), "right": (0, 1), "down": (1, 0), "left": (0, -1)}
total_nice_kids = 0

for row in range(n):
    line = input().split()
    for col in range(n):
        if line[col] == "S":
            santa_pos = [row, col]
        if line[col] == "V":
            total_nice_kids += 1
    matrix.append(line)

while True:
    line = input()
    if line == "Christmas morning":
        break

    dir_changes = directions[line]
    new_pos = [santa_pos[0] + dir_changes[0], santa_pos[1] + dir_changes[1]]

    if matrix[new_pos[0]][new_pos[1]] == "V":
        presents -= 1
    elif matrix[new_pos[0]][new_pos[1]] == "C":
        dropped_presents = drop_presents(new_pos, matrix, presents)
        presents -= dropped_presents

    matrix[santa_pos[0]][santa_pos[1]] = "-"
    santa_pos = new_pos
    matrix[santa_pos[0]][santa_pos[1]] = "S"

    if presents <= 0 and get_nice_kids(matrix):
        print("Santa ran out of presents!")
        break

    if not get_nice_kids(matrix):
        break

[print(" ".join(row)) for row in matrix]
nice_kids = get_nice_kids(matrix)

if nice_kids > 0:
    print(f"No presents for {nice_kids} nice kid/s.")
else:
    print(f"Good job, Santa! {total_nice_kids} happy nice kid/s.")