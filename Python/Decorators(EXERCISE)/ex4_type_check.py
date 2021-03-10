def type_check(typ):
    def decorator(func):

        def check_param(param, typ):
            return isinstance(param, typ)

        def wrapper(param):
            if not check_param(param, typ):
                return 'Bad Type'

            return func(param)

        return wrapper
    return decorator


@type_check(int)
def times2(num):
    return num*2


print(times2(2))
print(times2('Not A Number'))

@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
