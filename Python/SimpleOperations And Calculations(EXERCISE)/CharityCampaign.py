days = int(input())
bakers = int(input())
cakes_number = float(input())
gofrets_number = float(input())
pancakes_number = float(input())

cakes_price = 45
gofrets_price = 5.80
pancakes_price = 3.20

one_baker_cakes = cakes_number * cakes_price
one_baker_pancakes = pancakes_number * pancakes_price
one_baker_gofrets = gofrets_number * gofrets_price

all_money = (days * bakers) * (one_baker_cakes + one_baker_gofrets + one_baker_pancakes)
money_for_products = 1/8 * all_money
money_for_charity = all_money - money_for_products

print(f"{money_for_charity:.2f}")