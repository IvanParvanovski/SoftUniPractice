def squares(n):
    # for i in range(1, n + 1):
    #     yield i * i

    return (x * x for x in range(1, n + 1))



a = list(squares(5))
print(list(squares(5)))


