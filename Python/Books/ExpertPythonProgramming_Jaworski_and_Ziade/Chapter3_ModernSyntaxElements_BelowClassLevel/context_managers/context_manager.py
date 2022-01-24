with open('./words.txt', 'r') as hosts:
    for line in hosts:
        if line.startswith('#'):
            continue
        print(line.strip())
