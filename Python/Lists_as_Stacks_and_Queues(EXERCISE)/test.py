shop = dict()
fruit_dict = dict()

fruit = input()
while fruit != "End":
    fruit_dict[fruit] = 0
    fruit = input()

print(fruit_dict)
shop["products"] = fruit_dict
print(shop)

for item in shop:
    products = shop[item]
    for key, value in products.items():
        print(f"{key} -> {value}")