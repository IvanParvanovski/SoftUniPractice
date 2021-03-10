num = int(input())

for i in range(num):
    for k in range(num):
        for j in range(num):

            print(f"{chr(i + 97)}{chr(k + 97)}{chr(j + 97)}")