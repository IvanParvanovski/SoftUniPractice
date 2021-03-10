days_competition = int(input())
sport = ""
win_or_lose = ""
win_counter = 0
lose_counter = 0
full_win_counter = 0
full_lose_counter = 0
total = 0
sum = 0

for counter in range(days_competition):

    while sport != "Finish":
        sport = input()
        if sport == "Finish":
            break
        win_or_lose = input()

        if win_or_lose == "win":
            total += 20
            win_counter += 1
            full_win_counter += 1
        else:
            lose_counter += 1
            full_lose_counter += 1

    if win_counter > lose_counter:
        sum += 10/100 * total
    sum += total

    lose_counter = 0
    win_counter = 0
    total = 0
    sport = ""

if full_win_counter > full_lose_counter:
    sum += 20 / 100 * sum
    print(f"You won the tournament! Total raised money: {sum:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {sum:.2f}")
