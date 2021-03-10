items = input().split()
bakery_dict = dict()

for index in range(0, len(items), 2):
    bakery_dict[items[index]] = int(items[index + 1])

print(bakery_dict)
