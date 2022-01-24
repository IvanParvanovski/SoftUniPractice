from threading import RLock

lock = RLock()


def synchronized(function):
    def _synchronized(*args, **kwargs):
        lock.acquire()
        try:
            return function(*args, **kwargs)
        finally:
            lock.release()
    return _synchronized

@synchronized
def thread_safe():
    pass
