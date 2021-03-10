class ValueCannotBeNegative(Exception):
    pass


n = 5
for _ in range(n):
    num = int(input())
    if num < 0:
        raise ValueCannotBeNegative