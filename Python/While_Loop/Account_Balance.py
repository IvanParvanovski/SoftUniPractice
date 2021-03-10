balance_count = int(input())
x = 1
total = 0
money_increase = 0

while x <= balance_count:
    money_increase = float(input())

    if money_increase > 0:
        print(f"Increase: {money_increase:.2f}")
        x += 1
    else:
        print(f"Invalid operation!")
        break
    total += money_increase

print(f"Total: {total:.2f}")
