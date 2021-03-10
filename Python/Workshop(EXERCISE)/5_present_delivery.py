def create_neighborhood(size):
    matrix = list()
    for rows in range(size):
        matrix.append(input().split())
    return matrix


def find_santa(matrix):
    for row_index in range(len(matrix)):
        row = matrix[row_index]
        if "S" in row:
            column_index = row.index("S")
            return row_index, column_index


def all_good_kids(matrix):
    result = 0
    for row_index in range(len(matrix)):
        row = matrix[row_index]
        if "V" in row:
            result += row.count("V")
    return result

def define_new_position(direction_to_move_on, santa_location):
    row_to_move_on = direction_to_move_on[0]
    column_to_move_on = direction_to_move_on[1]
    santa_row = santa_location[0]
    santa_column = santa_location[1]
    new_row = row_to_move_on + santa_row
    new_column = santa_column + column_to_move_on
    return new_row, new_column


def is_new_position_valid(row, column, matrix):
    row_valid = False
    col_valid = False
    if -1 < row < len(matrix):
        row_valid = True
    if -1 < column < len(matrix):
        col_valid = True
    return row_valid and col_valid


def reached_cookie(row, column, matrix, direction, presents_count, delivered_presents_to_nice_kids):
    new_row, new_column = define_new_position(direction, (row, column))
    house = matrix[new_row][new_column]
    if house == "X" or house == "V":
        matrix[new_row][new_column] = "-"
        presents_count -= 1
    if house == "V":
        delivered_presents_to_nice_kids += 1
    return presents_count, delivered_presents_to_nice_kids


presents_count = int(input())
neighborhood_size = int(input())

neighborhood = create_neighborhood(neighborhood_size)
santa_position = find_santa(neighborhood)

directions = {"up": (-1, 0),
              "down": (1, 0),
              "left": (0, -1),
              "right": (0, 1)}

ran_out_of_presents = False
delivered_presents_to_nice_kids = 0

while True:
    if presents_count <= 0 and all_good_kids(neighborhood):
        ran_out_of_presents = True
        break

    command = input()
    if command == "Christmas morning":
        break

    new_row, new_column = define_new_position(directions[command], santa_position)
    if is_new_position_valid(new_row, new_column, neighborhood):
        santa_previous_row = santa_position[0]
        santa_previous_column = santa_position[1]
        neighborhood[santa_previous_row][santa_previous_column] = "-"
        house = neighborhood[new_row][new_column]
        neighborhood[new_row][new_column] = "S"

        if house == "V":
            delivered_presents_to_nice_kids += 1
            presents_count -= 1

        elif house == "C":
            for direction in directions.keys():
                if presents_count > 0:
                    presents_count, delivered_presents_to_nice_kids = reached_cookie(new_row, new_column, neighborhood,
                                                directions[direction], presents_count, delivered_presents_to_nice_kids)
                else:
                    ran_out_of_presents = True
                    break

        santa_position = new_row, new_column

if ran_out_of_presents:
    print("Santa ran out of presents!")
    [print(' '.join(row)) for row in neighborhood]
    nice_kids_amount = sum([row.count("V") for row in neighborhood])
    print(f"No presents for {nice_kids_amount} kid/s.")

else:
    [print(' '.join(row)) for row in neighborhood]
    print(f"Good job, Santa! {delivered_presents_to_nice_kids} happy nice kid/s.")
