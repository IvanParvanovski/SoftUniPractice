original_list = [
    [1, 2, 3],
    [4, 5, 6],
]

original_dict = {
    'one': [1, 2, 3],
    'two': [4, 5, 6],
}

original_set = {
    1, 2, 3,
    4, 5, 6,
}

original_tuple = (
    [1, 2, 3],
    [4, 5, 6]
)


new_list = list(original_list)
new_dict = dict(original_dict)
new_set = set(original_set)
new_tuple = tuple(original_tuple)

print(new_list)
print(new_dict)
print(new_set)
print(new_tuple)
