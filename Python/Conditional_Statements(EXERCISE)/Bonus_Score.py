num = int(input())
score = 0

if num <= 100:
    score += 5
if num > 100 and num < 1000:
    score += 20/100 * num
if num > 1000:
    score += 10/100 * num
if num % 2 == 0:
    score += 1
if num % 10 == 5:
    score += 2

num += score
print(score)
print(num)
