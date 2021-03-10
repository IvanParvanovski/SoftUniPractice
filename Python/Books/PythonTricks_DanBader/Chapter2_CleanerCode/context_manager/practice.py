import time


def my_func():
    return [_ for _ in range(100000)]


class MeasureTime:
    def __init__(self, func):
        self.func = func

    def __enter__(self):
        self.start_time = time.perf_counter()
        self.func()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.perf_counter() - self.start_time

# def measure_time(func):
#     start = time.perf_counter()
#     func()
#     end = time.perf_counter()
#     return end - start


with MeasureTime(my_func) as measure:
    pass


print(measure.end_time)
