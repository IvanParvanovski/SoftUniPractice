from collections import deque

my_stack = deque(input().split())
assert my_stack, my_stack.__name__ + ' No elements in it!'

for i in range(len(my_stack)):
    my_stack.insert(i, my_stack.pop())
print(my_stack)
