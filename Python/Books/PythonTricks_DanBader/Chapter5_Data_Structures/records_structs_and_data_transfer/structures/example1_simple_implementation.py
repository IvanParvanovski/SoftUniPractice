from struct import Struct
from sys import getsizeof

MyStruct = Struct('i?f')
data = MyStruct.pack(23, False, 42.0)

# All you get is a blob of data:
print(data)

# Data blobs can be unpacked again
print(MyStruct.unpack(data))

# Optimization - takes a little amount of memory
my_tuple = (23, False, 42.0)
print(getsizeof(data))
print(getsizeof(my_tuple))
