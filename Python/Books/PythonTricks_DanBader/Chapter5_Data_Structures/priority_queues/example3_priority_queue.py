from queue import PriorityQueue

my_que = PriorityQueue()

my_que.put((2, 'code'))
my_que.put((1, 'sleep'))
my_que.put((3, 'eat'))

while not my_que.empty():
    print(my_que.get())
