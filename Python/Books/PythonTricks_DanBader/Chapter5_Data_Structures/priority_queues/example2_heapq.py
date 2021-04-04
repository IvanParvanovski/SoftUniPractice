import heapq

my_que = list()

heapq.heappush(my_que, (2, 'code'))
heapq.heappush(my_que, (1, 'eat'))
heapq.heappush(my_que, (3, 'sleep'))

while my_que:
    print(heapq.heappop(my_que))
