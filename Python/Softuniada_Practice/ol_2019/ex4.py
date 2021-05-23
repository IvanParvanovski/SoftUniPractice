matrix_size = int(input())
field = list()

for _ in range(matrix_size):
    field.append([x.split() for x in input().split(' | ')])

melons_order = {
    'W': 'E',
    'E': 'F',
    'F': 'A',
    'A': 'W',
}

while True:
    user_input = input()

    if user_input == 'Melolemonmelon':
        break

    harvest_layer, harvest_row, harvest_column = map(int, user_input.split())

    field[harvest_row][harvest_layer][harvest_column] = '0'

    for row_index, row in enumerate(field):
        for layer_index, layer in enumerate(row):
            for column_index, column in enumerate(layer):

                # Up
                if row_index == harvest_row - 1 and \
                        column_index == harvest_column and \
                        layer_index == harvest_layer:

                    continue

                # Left
                elif row_index == harvest_row and \
                        column_index == harvest_column - 1 and \
                        layer_index == harvest_layer:

                    continue

                # Right
                elif row_index == harvest_row and \
                        column_index == harvest_column + 1 and \
                        layer_index == harvest_layer:

                    continue

                # Down
                elif row_index == harvest_row + 1 and \
                        column_index == harvest_column and \
                        layer_index == harvest_layer:

                    continue

                # Back
                elif row_index == harvest_row and \
                        column_index == harvest_column and \
                        layer_index == harvest_layer - 1:

                    continue

                # Front
                elif row_index == harvest_row and \
                        column_index == harvest_column and \
                        layer_index == harvest_layer + 1:

                    continue

                else:
                    field[row_index][layer_index][column_index] = melons_order.get(column, '0')

for row in field:
    print(' | '.join(' '.join(layer) for layer in row))
