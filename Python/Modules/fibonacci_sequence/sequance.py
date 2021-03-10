def create_sequence(n):
    if n == 0:
        return list('0')
    self_sequence = [0, 1]
    for i in range(2, n):
        self_sequence.append(self_sequence[i - 2] + self_sequence[i - 1])
    return [str(x) for x in self_sequence]
