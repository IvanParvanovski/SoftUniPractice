from sys import version_info

print('This is Python {}.{}'.format(*version_info))
print('This is Python {0}.{1}'.format(*version_info))
print('This is Python {major}.{minor}'.format(major=version_info.major,
                                              minor=version_info.minor))

print(f'This is Python {version_info.major}.{version_info.minor}')


for x in range(10):
    print(f'10 ^ x == {10 ** x:10d}')
