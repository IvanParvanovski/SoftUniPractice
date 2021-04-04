from queue import Queue

my_que = Queue()

my_que.put('eat')
my_que.put('sleep')
my_que.put('code')

print(my_que)

print(my_que.get_nowait())
print(my_que.get())

print(my_que.get_nowait())
print('Hello1')

print(my_que.get())
print('Hello2')
