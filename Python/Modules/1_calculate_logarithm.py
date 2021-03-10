from math import log


def calculate_log(x, base):
    if base == "natural":
        return log(x)
    else:
        return log(x, int(base))


print(f"{calculate_log(int(input()), input()):.2f}")
