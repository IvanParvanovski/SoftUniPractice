from collections import deque

start_name = input()
end_name = input()

name_to_change = deque(start_name)
name_to_change.appendleft(name_to_change.pop())

counter = 1
can_change = True
while True:
    full_name = ''.join(name_to_change)
    if full_name == end_name:
        break

    if full_name == start_name:
        can_change = False
        break

    name_to_change.appendleft(name_to_change.pop())
    counter += 1

if can_change:
    print(f'The minimum operations required to convert '
          f'"{start_name}" to "{"".join(name_to_change)}" are {counter}')
else:
    print('The name cannot be transformed!')