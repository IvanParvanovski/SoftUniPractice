def solve(queries, stack):
    for _ in range(queries):
        raw_input = input().split()
        command = int(raw_input[0])

        if command == 1:
            number = int(raw_input[1])
            stack.append(number)

        elif command == 2:
            if len(stack) != 0:
                stack.pop()

        elif command == 3:
            if len(stack) != 0:
                print(max(stack))

        elif command == 4:
            if len(stack) != 0:
                print(min(stack))
    return ', '.join(map(str, reversed(stack)))


print(solve(int(input()), list()))
