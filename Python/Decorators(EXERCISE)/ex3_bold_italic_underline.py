def format_text(typ_start, typ_end, func, args):
    return f'{typ_start}{func(*args)}{typ_end}'


def make_bold(func):
    def wrapper(*args):
        typ_start = '<b>'
        typ_end = '</b>'
        return format_text(typ_start, typ_end, func, args)

    return wrapper


def make_italic(func):
    def wrapper(*args):
        typ_start = '<i>'
        typ_end = '</i>'
        return format_text(typ_start, typ_end, func, args)

    return wrapper


def make_underline(func):
    def wrapper(*args):
        typ_start = '<u>'
        typ_end = '</u>'
        return format_text(typ_start, typ_end, func, args)

    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"

print(greet("Peter"))
@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"


print(greet_all("Peter", "George"))
