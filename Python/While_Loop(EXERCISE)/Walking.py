total = 0
steps = ""

while total < 10000 and steps != "Going home":
    steps = input()

    if steps == "Going home":
        steps = input()
        int_steps = int(steps)
        total += int_steps
        break
    else:
        int_steps = int(steps)
        total += int_steps

if total >= 10000:
    print("Goal reached! Good job!")
elif total < 10000:
    deff = 10000 - total
    print(f"{deff} more steps to reach goal.")