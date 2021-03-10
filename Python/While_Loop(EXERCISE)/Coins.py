money_machine_gives = float(input())
money_at_coins = money_machine_gives * 100
coins = 0
while money_at_coins > 0:
    while money_at_coins >= 200:
        coins += 1
        money_at_coins -= 200
    while 100 <= money_at_coins < 200:
        coins += 1
        money_at_coins -= 100
    while 50 <= money_at_coins < 100:
        coins += 1
        money_at_coins -= 50
    while 20 <= money_at_coins < 50:
        coins += 1
        money_at_coins -= 20
    while 10 <= money_at_coins < 20:
        coins += 1
        money_at_coins -= 10
    while 5 <= money_at_coins < 10:
        coins += 1
        money_at_coins -= 5
    while 2 <= money_at_coins < 5:
        coins += 1
        money_at_coins -= 2
    while 1 <= money_at_coins < 2:
        coins += 1
        money_at_coins -= 1
    break
print(coins)
