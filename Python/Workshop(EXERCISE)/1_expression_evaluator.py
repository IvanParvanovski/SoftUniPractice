from collections import deque
from math import floor
string_expression = deque(input().split())

operators = {'*',
             '+',
             '-',
             '/'}

numbers_to_operate = list()


final_result = 0
while string_expression:
    element = string_expression.popleft()
    if element in operators:
        final_result = floor(eval(f'{element}'.join(numbers_to_operate)))
        string_expression.appendleft(str(final_result))
        numbers_to_operate.clear()
    else:
        numbers_to_operate.append(element)


print(final_result)