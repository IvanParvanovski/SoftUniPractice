user_product = input()
user_quantity = int(input())


def coffee(quantity):
    coffee_price = 1.50
    return coffee_price * quantity


def water(quantity):
    water_price = 1.00
    return water_price * quantity


def coke(quantity):
    coke_price = 1.40
    return coke_price * quantity


def snacks(quantity):
    snacks_price = 2.00
    return snacks_price * quantity


def calculations(main_product, quantity):
    mapping = [
        ["coffee", coffee],
        ["water", water],
        ["coke", coke],
        ["snacks", snacks]
    ]

    for for_product, function in mapping:
        if for_product == main_product:
            return function(quantity)


print(f"{calculations(user_product, user_quantity):.2f}")