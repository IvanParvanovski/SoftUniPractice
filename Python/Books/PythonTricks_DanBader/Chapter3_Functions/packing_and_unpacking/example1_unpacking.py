def print_vectors(x, y, z):
    print('<%s, %s, %s>' % (x, y, z))


tuple_vec = (1, 2, 3, )

list_vec = [1, 2, 3, ]

set_vec = {1, 2, 3, }

dict_vec = {
    'x': 1,
    'y': 2,
    'z': 3,
}

print_vectors(*tuple_vec)
print_vectors(*list_vec)
print_vectors(*set_vec)
print_vectors(**dict_vec)
