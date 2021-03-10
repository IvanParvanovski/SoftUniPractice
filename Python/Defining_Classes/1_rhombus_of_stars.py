def generate_line(index, n):
    indent = ' ' * (n - index - 1)
    stars = "* " * (index + 1)
    return f"{indent}{stars}"


def generate_rhombus(n):
    result = ""
    for i in range(n):
        result += f"{generate_line(i, n)}\n"

    for i in range(n - 2, -1, -1):
        result += f"{generate_line(i, n)}\n"

    return result[:-1]


star = int(input())
print(generate_rhombus(star))
