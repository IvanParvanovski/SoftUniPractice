numbers = input().split(", ")
group = 10
while len(numbers) > 0:
    local_list = list()
    for element in numbers:
        if int(element) <= group:
            local_list.append(element)
    for element in local_list:
        numbers.remove(element)
    print(f"Group of {group}'s: {list(map(int, local_list))}")
    group += 10
    max()
