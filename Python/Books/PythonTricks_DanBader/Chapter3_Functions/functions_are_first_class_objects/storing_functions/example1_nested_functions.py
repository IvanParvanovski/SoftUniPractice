def yell(text):
    return text.upper() + '!'


bark = yell
funcs = [bark, str.lower, str.capitalize]
print(funcs)

for f in funcs:
    print(f'{f.__name__}\n'
          f'{f("hey there")}\n'
          f'{f}\n')


print(funcs[0]('Woof'))