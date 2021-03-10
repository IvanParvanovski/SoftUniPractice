def foo(required, *args, **kwargs):
    print(required)
    if args:
        print(args)
    if kwargs:
        print(kwargs)
    print()


foo('hello')
foo('hello', 1, 2, 3)
foo('hello', 1, 2, 3, name='Ivan', age=15)