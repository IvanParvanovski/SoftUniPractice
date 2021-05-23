# Bytes
print(bytes([102, 111, 111]))

# Bytes as collection
print(list(bytes([102, 111, 111])))
print(list(b'foo'))
print(tuple(b'foo'))

# b or B prefix
print(type('some string'))
print(type(b'some string'))
print(type(B'some string'))
