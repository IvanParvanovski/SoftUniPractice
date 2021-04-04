from multiprocessing import Queue

my_que = Queue()

print(my_que)

my_que.put('eat')
my_que.put('sleep')
my_que.put('code')

print(my_que.get())
print(my_que.get())
print(my_que.get_nowait())
print('Hello1')

print(my_que.get())
print('Hello2')

