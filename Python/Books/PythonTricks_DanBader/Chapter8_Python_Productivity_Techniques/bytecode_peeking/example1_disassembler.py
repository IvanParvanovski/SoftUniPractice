import dis


def greet(name):
    return 'Hello, ' + name + '!'


print(greet.__code__)
print(greet.__code__.co_consts)
print(greet.__code__.co_varnames)

print(greet('Guido'))

dis.dis(greet)
