queue = list()

queue.append((2, 'code'))
queue.append((1, 'eat'))
queue.append((3, 'sleep'))

# NOTE: Remember to re-sort every time
#       a new element is inserted, or use
#       bisect.insort()

queue.sort(reverse=True)

while queue:
    print(queue.pop())
