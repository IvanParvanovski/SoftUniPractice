my_stack = list()

queries = int(input())
for _ in range(queries):
    current_query = [int(x) for x in input().split()]

    command = current_query[0]
    assert 0 < command < 5, 'Invalid command!'

    if command == 1:
        my_stack.append(current_query[1])
    elif command == 2:
        if my_stack:
            my_stack.pop()
    elif command == 3:
        print(max(my_stack))
    elif command == 4:
        print(min(my_stack))

print(', '.join((str(x) for x in my_stack)))
