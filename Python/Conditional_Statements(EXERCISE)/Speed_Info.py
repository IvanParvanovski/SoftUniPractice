num = float(input())
speed = ""

if num <= 10:
    speed = "slow"
if num > 10 and num <= 50:
    speed = "average"
if num > 50 and num <= 150:
    speed = "fast"
if num > 150 and num <= 1000:
    speed = "ultra fast"
if num > 1000:
    speed = "extremely fast"

print(speed)
