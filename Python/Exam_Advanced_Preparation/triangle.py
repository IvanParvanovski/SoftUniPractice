def get_magic_triangle(number):
    if number > 0:
        local_matrix = [[1]]
        for num_index in range(1, number):
            new_numbers = [1, 1]
            previous_matrix = local_matrix[num_index - 1]
            for previous_matrix_index in range(len(previous_matrix) - 1):
                x = previous_matrix[previous_matrix_index]
                y = previous_matrix[previous_matrix_index + 1]
                new_numbers.insert(1, x + y)
            local_matrix.append(new_numbers)
        return local_matrix
    return list

