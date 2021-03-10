input_divisor = int(input())
input_bound = int(input())
num = 0

for num in range(input_bound, 0, -1):
    if num % input_divisor == 0:
        break
print(num)