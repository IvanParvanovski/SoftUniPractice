import threading
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second...')
    time.sleep(seconds)
    print('Done sleeping...')


threads = list()
for _ in range(10):
    t = threading.Thread(target=do_something, args=[3])
    t.start()
    threads.insert(0, t)
threads[0].join()

finish = time.perf_counter()
print(f'Finished in {round(finish - start, 2)} second(s)')
