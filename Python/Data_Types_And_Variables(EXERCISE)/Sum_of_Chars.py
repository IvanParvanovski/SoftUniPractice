chars = int(input())
total = 0

for chars_counter in range(chars):
    symbol = input()
    total += ord(symbol)
print(f"The sum equals: {total}")