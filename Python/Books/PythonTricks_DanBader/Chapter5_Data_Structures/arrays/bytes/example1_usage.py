arr = bytes((1, 2, 3, 48, 89, 213, 123))
print(arr)
print(arr[1])

# broken_arr = bytes((0, 300))
arr_2 = b'\x00\x01\x02\x03'
print(arr_2)
print(arr_2[1])

# Immutable
# arr[1] = 23
# del arr[1]
