vowels = frozenset({'a', 'e', 'i', 'o', 'u'})
print(vowels)

# Frozensets are immutable
# vowels.add('p')

# Frozensets are hashable and can
# be used as dictionary keys:
d = {frozenset({1, 2, 3}): 'hello'}
print(d)
print(d[frozenset({1, 2, 3})])
