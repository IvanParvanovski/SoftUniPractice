from collections import deque

bombs_types_and_price = {40: "Datura Bombs",
                         60: "Cherry Bombs",
                         120: "Smoke Decoy Bombs", }

bombs_count = {"Datura Bombs": 0,
               "Cherry Bombs": 0,
               "Smoke Decoy Bombs": 0}


bombs_check = {"Datura Bombs": False,
               "Cherry Bombs": False,
               "Smoke Decoy Bombs": False}

bomb_effects = deque([int(x) for x in input().split(', ')])
bomb_casings = [int(x) for x in input().split(', ')]
pouched_filled = False

while bomb_effects and bomb_casings:
    for b in bombs_count:
        if bombs_count[b] >= 3:
            bombs_check[b] = True

    if False in bombs_check.values():
        bomb_eff = bomb_effects.popleft()
        bomb_cas = bomb_casings.pop()
        bomb_sum = bomb_cas + bomb_eff

        if bomb_sum in bombs_types_and_price:
            bomb = bombs_types_and_price[bomb_sum]
            bombs_count[bomb] += 1
        else:
            bomb_effects.appendleft(bomb_eff)
            bomb_casings.append(bomb_cas - 5)
    else:
        pouched_filled = True
        break

pouch_message = ""
if pouched_filled:
    pouch_message = "Bene! You have successfully filled the bomb pouch!"

else:
    pouch_message = "You don't have enough materials to fill the bomb pouch."

print(pouch_message)


print(f"Bomb Effects: {', '.join([str(x) for x in bomb_effects])}" if bomb_effects else "Bomb Effects: empty")
print(f"Bomb Casings: {', '.join([str(x) for x in bomb_casings])}" if bomb_casings else "Bomb Casings: empty")
sorted_bombs = sorted(bombs_count)

for bomb in sorted_bombs:
    print(f"{bomb}: {bombs_count[bomb]}")
