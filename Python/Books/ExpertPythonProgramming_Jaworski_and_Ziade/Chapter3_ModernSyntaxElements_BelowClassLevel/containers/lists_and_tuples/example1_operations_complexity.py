my_list = [1, 2, 3]

# Copy -> O(n)
my_list_copy = list(my_list)

# Append -> O(1)
my_list.append(4)

# Insert -> O(n)
my_list.insert(0, 10)

# Get item -> O(1)
print(my_list[2])

# Set item -> O(1)
my_list[2] = 80

# Delete item -> O(n)
del my_list[4]

# Iteration -> O(n)
a = (x for x in my_list)

# Get slice of length k -> O(k)
print(my_list[:2])

# Set slice of length k -> O(k + n)
my_list[:2] = (99, 100)

# Delete slice -> O(n)
del my_list[:2]

# Extend -> O(k)
my_list.extend((4, 5, 6))

# Multiply by k -> O(n * k)
print(my_list * 2)

# Test existence (element in list) -> O(n)
print(6 in my_list)

# min() / max() -> O(n)
print(min(my_list))
print(max(my_list))

# Get length -> O(1)
print(len(my_list))
