def clothe_store(clothes_values, capacity):
    sum = 0
    racks = 1
    while clothes_values:
        element = int(clothes_values.pop())
        if sum + element == capacity and len(clothes_values) != 0:
            sum = 0
            racks += 1
        elif sum + element > capacity:
            sum = element
            racks += 1
        else:
            sum += element
    return racks


print(clothe_store(input().split(), int(input())))