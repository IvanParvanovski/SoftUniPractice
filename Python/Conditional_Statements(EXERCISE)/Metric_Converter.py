num = float(input())
input1 = input()
output = input()

if input1 == "mm" and output == "cm":
    num /= 10
if input1 == "mm" and output == "m":
    num /= 1000
if input1 == "cm" and output == "mm":
    num *= 10
if input1 == "cm" and output == "m":
    num /= 100
if input1 == "m" and output == "mm":
    num *= 1000
if input1 == "m" and output == "cm":
    num *= 100

print(f"{num:.3f}")