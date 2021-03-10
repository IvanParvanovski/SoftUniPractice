lilies_age = int(input())
laundry_price = float(input())
one_toy_price = int(input())
toys_counter = 0
money_total = 0
money_price = 10

for i in range(1, lilies_age + 1):
    if i % 2 == 0:
        money_total += money_price
        money_price += 10
    else:
        toys_counter += 1
    if i >= 2 and i % 2 == 0:
        money_total -= 1
full_money = money_total + toys_counter * one_toy_price

if full_money >= laundry_price:
    diff = full_money - laundry_price
    print(f"Yes! {diff:.2f}")
else:
    diff = laundry_price - full_money
    print(f"No! {diff:.2f}")