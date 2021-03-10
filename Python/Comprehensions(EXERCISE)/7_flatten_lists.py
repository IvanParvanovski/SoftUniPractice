line = input()
result = [el for x in line.split("|")[::-1] for el in x.split(" ") if el != ""]
print(' '.join(result))