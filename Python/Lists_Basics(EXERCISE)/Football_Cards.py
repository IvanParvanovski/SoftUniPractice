cards = input().split()
team_A = list(range(1, 12))
team_B = list(range(1, 12))
team_A_length = len(team_A)
team_B_length = len(team_B)

for card in cards:
    tokens = card.split("-")
    team = tokens[0]
    player = int(tokens[1])

    if team == "A":
        if player in team_A:
            team_A.remove(player)

            if team_A_length < 7:
                break
        else:
            continue
    elif team == "B":
        if player in team_B:
            team_B.remove(player)

            if team_B_length < 7:
                break
        else:
            continue

team_A_length = len(team_A)
team_B_length = len(team_B)
print(f"Team A - {team_A_length}; Team B - {team_B_length}")
if team_A_length < 7 or team_B_length < 7:
    print("Game was terminated")
