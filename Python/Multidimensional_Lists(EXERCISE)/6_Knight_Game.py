def is_valid(position, size):
    row = position[0]
    col = position[1]
    return 0 <= row < size and 0 <= col < size


def get_killed_knights(row, col, size, board):
    killed_knights = 0
    rows = [-2, -1, 1, 2, 2, 1, -1, -2]
    cols = [1, 2, 2, 1, -1, -2, -2, -1]
    for i in range(8):
        current_position = [row + rows[i], col + cols[i]]
        if is_valid(current_position, size) and board[current_position[0]][current_position[1]] == "K":
            killed_knights += 1
    return killed_knights


n = int(input())
board = []
total_kills = 0

for _ in range(n):
    board.append([x for x in input()])

while True:
    most_kills = 0
    to_kill = []

    for row in range(n):
        for col in range(n):
            if board[row][col] == "K":
                killed_knights = get_killed_knights(row, col, n, board)
                if killed_knights > most_kills:
                    most_kills = killed_knights
                    to_kill = [row, col]

    if most_kills == 0:
        break

    board[to_kill[0]][to_kill[1]] = "0"
    total_kills += 1

print(total_kills)