from array import array

# arr = array('i', (1.0, 1.5, 2.0, 2.5))
arr = array('f', (1.0, 1.5, 2.0, 2.5))
print(arr[1])

# Nice representation
print(arr)

# Mutable
arr[1] = 23
print(arr)

del arr[1]
print(arr)

arr.append(98765)
print(arr)

arr[1] = 'hello'
print(arr)
