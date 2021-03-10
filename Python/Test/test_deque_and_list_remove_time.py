import time
from collections import deque


def detect_time(func):
    def wrapper(num):
        detect_time_start = time.process_time()
        func(num)
        detect_time_end = time.process_time()
        executed_time = detect_time_end - detect_time_start
        return executed_time

    return wrapper


@detect_time
def list_func(num):
    my_list = list()
    for i in range(num):
        my_list.append(num)

    my_list.pop()
    my_list.pop()
    my_list.pop()
    print(my_list[-1])


@detect_time
def deque_func(num):
    my_deque = deque()
    for i in range(num):
        my_deque.appendleft(num)

    my_deque.popleft()
    my_deque.popleft()
    my_deque.popleft()
    print(my_deque[0])


n = 10000000
print(f'List time: {list_func(n)}')
print(f'Deque time: {deque_func(n)}')
