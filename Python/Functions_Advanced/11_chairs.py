def chairs_combinations(names, size, result=[]):
    if len(result) == size:
        print(', '.join(result))
        return

    for i in range(len(names)):
        name = names[i]
        result.append(name)
        chairs_combinations(names[i + 1:], size, result)
        result.pop()


people_names = input().split(', ')
couples = int(input())
chairs_combinations(people_names, couples)
