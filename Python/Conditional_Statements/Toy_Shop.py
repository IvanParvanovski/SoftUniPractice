trip_prize = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())
deff = 0

puzzles_price = 2.60
dolls_price = 3
bears_price = 4.10
minions_price = 8.20
trucks_price = 2

all_toys = puzzles + dolls + bears + minions + trucks
money_sheGet = float((puzzles * puzzles_price) + (dolls * dolls_price) + (bears * bears_price) + (minions * minions_price) + (trucks * trucks_price))

if all_toys >= 50:
    money_sheGet = money_sheGet - 25/100 * money_sheGet

money_sheGet = money_sheGet - ((10/100) * money_sheGet)

if money_sheGet >= trip_prize:
    deff = money_sheGet - trip_prize
    print(f"Yes! {deff:.2f} lv left.")
else:
    deff = trip_prize - money_sheGet
    print(f"Not enough money! {deff:.2f} lv needed.")