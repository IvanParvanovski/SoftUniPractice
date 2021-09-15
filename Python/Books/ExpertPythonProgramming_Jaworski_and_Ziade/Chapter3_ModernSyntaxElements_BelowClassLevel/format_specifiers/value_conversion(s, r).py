class Data:
    def __str__(self):
        return 'str'

    def __repr__(self):
        return 'repr'


print('%s %r' % (Data(), Data(), ))
print('{0!s} {0!r}'.format(Data()))
print(f'{Data()!s} {Data()!r}')
