budget = float(input())
stoke = input()
stoke_count = int(input())

ballon_counter = 0
flowers_counter = 0
candles_counter = 0
ribbon_counter = 0
full_stoke_counter = 0
total = 0

while stoke != "stop" or total < budget:
    if stoke == "balloons":
        total += stoke_count * 0.1
        ballon_counter += stoke_count
    elif stoke == "flowers":
        flowers_counter += stoke_count
        total += stoke_count * 1.5
    elif stoke == "candles":
        total += stoke_count * 0.5
        candles_counter += stoke_count
    elif stoke == "ribbon":
        ribbon_counter += stoke_count
        total += stoke_count * 2
    if total >= budget:
        break

    stoke = input()
    if stoke == "stop":
        break
    stoke_count = int(input())

if budget <= total:
    print("All money is spent!")
else:
    diff = budget - total
    left_money = budget - diff
    print(f"Spend money: {left_money:.2f}")
    print(f"Money left: {diff:.2f}")

print(f"Purchased decoration is {ballon_counter} balloons, {ribbon_counter} m ribbon, {flowers_counter} flowers and {candles_counter} candles.")