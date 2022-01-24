hosts = open('./words.txt')
try:
    for line in hosts:
        if line.startswith('#'):
            continue
        print(line.strip())
finally:
    hosts.close()
