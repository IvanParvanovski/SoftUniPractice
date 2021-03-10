money_for_film = float(input())
actors = int(input())
one_cloth_money = float(input())
money_Left = 0

decor = 10 / 100 * money_for_film

actors_money = actors * one_cloth_money

if actors >= 150:
    actors_money -= 10 / 100 * actors_money

sum = actors_money + decor

if money_for_film > sum:
    money_Left = money_for_film - sum
else:
    money_Left = sum - money_for_film

if money_for_film >= sum:
    print("Action!")
    print(f"Wingard starts filming with {money_Left:.2f} leva left.")

if money_for_film < sum:
    print("Not enough money!")
    print(f"Wingard needs {money_Left:.2f} leva more.")
