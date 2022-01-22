"""
This module provides simple memoization arguments
that is able to store cached return result of
decorated function for specified period of time.
"""
import time
import hashlib
import pickle

cache = {}


def is_obsolete(entry, duration):
    """Check if given cache entry is obsolete"""
    return time.time() - entry['time'] > duration

def compute_key(function, args, kw):
    """Compute caching key for given value"""
    key = pickle.dumps((function.__name__, args, kw))
    return hashlib.sha1(key).hexdigest()


def memoize(duration=10):
    """
    Keyword-aware memoization decorator

    It allows to memoize function arguments for specified
    duration time.
    """

    def _memoize(function):
        def __memoize(*args, **kw):
            key = compute_key(function, args, kw)

            # do we have it already in cache?
            if (
                key in cache and
                not is_obsolete(cache[key], duration)
            ):
                # return cached value if it exists
                # and isn't too old
                print('we got a winner')
                return cache[key]['value']

            # compute result if there is no valid
            # cache available
            result = function(*args, **kw)
            # store the result ofr later use
            cache[key] = {
                'value': result,
                'time': time.time()
            }
            return result
        return __memoize
    return _memoize


# @memoize()
# def very_very_very_complex_stuff(a, b):
#     # if your computer gets hot on this calculation
#     # consider stopping it
#     return a + b
#
#
# print(very_very_very_complex_stuff(2, 2))
# print(very_very_very_complex_stuff(2, 2))

@memoize(1)
def very_very_very_complex_stuff(a, b):
    # if your computer gets hot on this calculation
    # consider stopping it
    return a + b


print(very_very_very_complex_stuff(2, 2))
print(very_very_very_complex_stuff(2, 2))

print(cache)

time.sleep(2)
print(very_very_very_complex_stuff(2, 2))
