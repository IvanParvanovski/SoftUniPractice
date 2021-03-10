from collections import defaultdict
products_dict = defaultdict(list)

args = input()
while args != "buy":
    args = args.split()

    product = args[0]
    price = float(args[1])
    quantity = int(args[2])

    if product in products_dict:
        products_dict[product][1] += quantity

        if price != products_dict[product][0]:
            products_dict[product][0] = price
    else:
        products_dict[product].extend((price, quantity))
    args = input()

for element in products_dict:
    print(f"{element} -> {products_dict[element][0] * products_dict[element][1]:.2f}")
