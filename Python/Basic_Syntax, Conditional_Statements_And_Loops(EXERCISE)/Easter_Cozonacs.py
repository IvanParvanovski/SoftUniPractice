user_budget = float(input()) # check
flour_price = float(input()) # check

eggs_price = 75 / 100 * flour_price # check
milk_price = flour_price + 25 / 100 * flour_price # check

cozonacs_counter = 0
colored_eggs_counter = 0
counter = 0

price_for_one_cozonac = flour_price + eggs_price + 1 / 4 * milk_price # check

while user_budget >= 0:
    user_budget -= price_for_one_cozonac
    if user_budget < 0:
        break
    else:
        cozonacs_counter += 1
        colored_eggs_counter += 3
        counter += 1

    if counter == 3:
        colored_eggs_counter -= cozonacs_counter - 2
        counter = 0

diff = user_budget % price_for_one_cozonac

print(f"You made {cozonacs_counter} cozonacs! Now you have {colored_eggs_counter} eggs and {diff:.2f}BGN left.")

