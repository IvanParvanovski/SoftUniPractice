a = [1, 2, 3]
b = a


print('A: %s' % a)
print('B: %s' % b)

print('a == b: ', a == b)
print('a is b: ', a is b)
print()

c = list(a)

print('A: %s' % a)
print('B: %s' % b)
print('C: %s' % c)

print('a == c: ', a == c)
print('a is c: ', a is c)
