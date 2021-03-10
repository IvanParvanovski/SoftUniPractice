num = int(input())
for digit in range(1, num + 1):
    sum = 0
    for index in range(len(str(digit))):
        sum += int(str(digit)[index])
    if sum == 5 or sum == 7 or sum == 11:
        true_false = True
    else:
        true_false = False
    print(f"{digit} -> {true_false}")