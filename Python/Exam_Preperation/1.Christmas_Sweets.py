baklava_price = float(input())
cupcakes_price = float(input())
shtolen_kgs = float(input())
candies_kgs = float(input())
biscuits_kgs = float(input())

shtolen_price = baklava_price + baklava_price * 0.60
full_shtolen_price = shtolen_price * shtolen_kgs

candies_price = cupcakes_price + cupcakes_price * 0.80
full_candies_price = candies_price * candies_kgs

full_biscuits_price = biscuits_kgs * 7.50
sum = full_biscuits_price + full_candies_price + full_shtolen_price
print(f"{sum:.2f}")
