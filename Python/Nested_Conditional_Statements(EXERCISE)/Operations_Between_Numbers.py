N1 = int(input())
N2 = int(input())
symbol = input()
sum = 0

if symbol == "+":
    sum = N1 + N2
elif symbol == "-":
    sum = N1 - N2
elif symbol == "*":
    sum = N1 * N2

elif symbol == "/":
    if N2 == 0:
        print(f"Cannot divide {N1} by zero")
    else:
        sum = N1 / N2
        print(f"{N1} / {N2} = {sum:.2f}")

elif symbol == "%":
    if N2 == 0:
        print(f"Cannot divide {N1} by zero")
    else:
        sum = N1 % N2
        print(f"{N1} % {N2} = {sum}")

if symbol == "+" or symbol == "-" or symbol == "*":

    if sum % 2 == 0:
        print(f"{N1} {symbol} {N2} = {sum} - even")
    else:
        print(f"{N1} {symbol} {N2} = {sum} - odd")
