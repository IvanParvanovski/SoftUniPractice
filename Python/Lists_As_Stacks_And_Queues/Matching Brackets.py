def expressions(expression):
    stack = list()
    result = list()

    for index in range(len(expression)):
        char = expression[index]
        if char == "(":
            stack.append(index)
        elif char == ")":
            start_index = stack.pop()
            result.append(expression[start_index:index + 1])
    return result


print('\n'.join(expression for expression in expressions(input())))