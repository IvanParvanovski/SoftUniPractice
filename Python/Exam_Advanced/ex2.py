def create_territory(size):
    matrix = list()
    for _ in range(size):
        matrix.append(list(input()))
    return matrix


def find_snake(matrix):
    for i in range(len(matrix)):
        row = matrix[i]
        if "S" in row:
            return i, row.index("S")


def check_position(matrix, row, col):
    if 0 <= row < len(matrix) and 0 <= col < len(matrix):
        return True
    else:
        return False


def check_food(quantity):
    return False if quantity >= 10 else True


def find_borrow(matrix):
    for i in range(len(matrix)):
        row = matrix[i]
        if "B" in row:
            return i, row.index("B")


territory_size = int(input())
territory = create_territory(territory_size)
snake_position = find_snake(territory)

food_quantity = 0

movement = {"up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1), }

while True:
    if not check_food(food_quantity):
        print("You won! You fed the snake.")
        break

    command = input()
    snake_last_position = snake_position
    snake_row = snake_position[0]
    snake_col = snake_position[1]

    snake_row += movement[command][0]
    snake_col += movement[command][1]

    snake_position = (snake_row, snake_col)

    if not check_position(territory, *snake_position):
        snake_last_row = snake_last_position[0]
        snake_last_col = snake_last_position[1]
        territory[snake_last_row][snake_last_col] = '.'
        print("Game over!")
        break

    token = territory[snake_row][snake_col]

    snake_last_row = snake_last_position[0]
    snake_last_col = snake_last_position[1]
    territory[snake_last_row][snake_last_col] = '.'

    if token == "*":
        food_quantity += 1

    elif token == "B":
        territory[snake_row][snake_col] = "."
        snake_row, snake_col = find_borrow(territory)
        snake_position = snake_row, snake_col

    territory[snake_row][snake_col] = "S"

print(f"Food eaten: {food_quantity}")
[print(''.join(row)) for row in territory]
