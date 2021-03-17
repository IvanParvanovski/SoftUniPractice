arr = 'abcd'
print(arr[1])
print(arr)

# Immutable

# arr[1] = 'j'
# del arr[1]

# Unpack string into list
mutable_arr = list(arr)

print('-'.join(mutable_arr))
print(type(arr))
print(type(arr[0]))
