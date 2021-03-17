arr = bytearray((1, 2, 3, 4))
print(arr[1])
print(arr)
print()

# Bytearrays are mutable
arr[1] = 255
print(arr[1])
print(arr)

print()

del arr[1]
print(arr[1])
print(arr)

print()

arr.append(123)
print(arr[-1])
print(arr)

# Bytearrays can only hold 'bytes'
# arr[1] = 'hello'
# print(arr)
#
# arr[1] = 300
# print(arr)

print()

# Copy
arr_second = bytes(arr)
print(arr_second)
