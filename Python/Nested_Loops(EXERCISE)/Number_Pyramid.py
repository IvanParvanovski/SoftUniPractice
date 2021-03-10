num = int(input())
current = 0

for row in range(1,num + 1):
    for colums in range(1, row + 1):
        current += 1
        if current > num:
            break
        print(str(current), end=" ")
    print()


