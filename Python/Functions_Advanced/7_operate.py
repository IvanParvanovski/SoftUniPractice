def operate(operator, *numbers):
    def get_initial_value(operator):
        if operator in ('+', '-'):
            return 0
        elif operator in ('*', '/'):
            return 1

    result = get_initial_value(operator)
    for x in numbers:
        if operator == '*':
            result *= x
        elif operator == "/":
            result /= x
        elif operator == "+":
            result += x
        elif operator == "-":
            result -= x

    return result
