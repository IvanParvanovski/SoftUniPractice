width = int(input())
lenght = int(input())
pieces_people_get = ""
total_pieces = 0

area = width * lenght

while total_pieces <= area:
    pieces_people_get = input()

    if pieces_people_get == "STOP":
        deff = area - total_pieces
        print(f"{deff} pieces are left.")
        break
    else:
        pieces_people_get = int(pieces_people_get)
        total_pieces += pieces_people_get

if total_pieces > area:
    deff = total_pieces - area
    print(f"No more cake left! You need {deff} pieces more.")
