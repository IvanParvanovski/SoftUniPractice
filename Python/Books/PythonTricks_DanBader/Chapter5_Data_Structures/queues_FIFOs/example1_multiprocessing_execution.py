from multiprocessing import Process, Queue
# from queue import Queue
from math import pow


def square(numbers, queue):
    for i in numbers:
        queue.put(f'Square: {pow(i, 2)}')


def cube(numbers, queue):
    for i in numbers:
        queue.put(f'Cube: {pow(i, 3)}')


if __name__ == '__main__':
    numbers = range(100)
    queue = Queue()

    square_process = Process(target=square, args=(numbers, queue))
    cube_process = Process(target=cube, args=(numbers, queue))

    square_process.start()
    cube_process.start()

    square_process.join()
    cube_process.join()

    while not queue.empty():
        print(queue.get())
