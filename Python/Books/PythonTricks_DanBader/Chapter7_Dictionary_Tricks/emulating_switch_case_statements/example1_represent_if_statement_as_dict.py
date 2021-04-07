def handle_a():
    print('Hi')


def handle_b():
    print('My name is')


def handle_default():
    print('Default!')


cond = input()

# if cond == 'cond_a':
#     handle_a()
# elif cond == 'cond_b':
#     handle_b()
# else:
#     handle_default()
#

func_dict = {
    'cond_a': handle_a,
    'cond_b': handle_b,
}

func_dict.get(cond, handle_default)()
