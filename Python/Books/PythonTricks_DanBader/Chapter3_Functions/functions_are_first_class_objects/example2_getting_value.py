from string import Template


def yell(text):
    return text.upper() + '!'


bark = yell

del yell

print(bark('woof'))

my_func_output = Template('Function name is $function_name')

print('Function name is %s' % bark.__name__)
print('Function name is {}'.format(bark.__name__))
print(f'Function name is {bark.__name__}')
print(my_func_output.substitute(function_name=bark.__name__))

print(yell('hello'))
