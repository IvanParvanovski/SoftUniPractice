import heapq
import time
from random import randint


def detect_time(func):
    def wrapper(li, n):
        detect_time_start = time.process_time()
        func(li, n)
        detect_time_end = time.process_time()
        executed_time = detect_time_end - detect_time_start
        return executed_time

    return wrapper


@detect_time
def heapify_speed(li, num):
    print('Heapify: ')

    heapq.heapify(li)
    for _ in range(num):
        print(heapq.heappop(li), end=', ')


@detect_time
def sort_speed(li, num):
    print('Sort: ')

    li = sorted(li)
    for _ in range(num):
        print(li.pop(0), end=', ')


# Test 1
# Heapify won!
# h_li = [randint(-257092, 247120987213) for _ in range(-10000, 1000000)]

# Test 2
# Sort won!
h_li = [*range(-1000000, 10000)]
s_li = h_li.copy()

print('\n', heapify_speed(h_li, 2))
print('*' * 20)
print('\n', sort_speed(s_li, 2))
