from collections import deque

my_que = deque()

my_que.append('eat')
my_que.append('sleep')
my_que.append('code')

print(my_que)

print(my_que.popleft())
print(my_que.popleft())
print(my_que.popleft())

print(my_que)

print(my_que.popleft())
