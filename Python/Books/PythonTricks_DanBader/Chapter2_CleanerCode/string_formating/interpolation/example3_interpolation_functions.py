# Behind the scenes
#
# def greet(name, question)
#     return ('Hello,' + name + ' How's it ' + question + '?')
#

import dis


def greet(name, question):
    return f"Hello, {name}! How's it {question}?"


name = 'Alek'
errno = 214
print(f"Hey {name}, there's {errno:#x} error!")

print(greet('Bob', 'going'))
print()
print(dis.dis(greet))