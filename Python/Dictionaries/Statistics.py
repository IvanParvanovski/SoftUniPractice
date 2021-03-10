user_input = input()
stocks = dict()
while user_input != "statistics":
    user_input = user_input.split(": ")

    product = user_input[0]
    quantity = user_input[1]

    if product in stocks:
        stocks[product] += int(quantity)
    else:
        stocks[product] = int(quantity)

    user_input = input()

print("Products in stock:")
print("\n".join(list(f"- {product}: {quantity}" for product, quantity in stocks.items())))
print(f"Total Products: {len(stocks)}")
print(f"Total Quantity: {sum(stocks.values())}")

