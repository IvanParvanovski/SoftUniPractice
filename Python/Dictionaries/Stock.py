items = input().split()
searched_stocks = input().split()

stocks = dict()

for index in range(0, len(items), 2):
    stocks[items[index]] = int(items[index + 1])


def searched_stock():
    output = ""
    for element in searched_stocks:
        if element in stocks and stocks[element] != 0:
            output = f"We have {stocks[element]} of {element} left"
        else:
            output = f"Sorry, we don't have {element}"
        print(output)


searched_stock()