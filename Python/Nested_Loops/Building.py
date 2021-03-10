floors = int(input())
rooms = int(input())

for floors_counter in range(floors, 0, -1):

    for rooms_counter in range(rooms):

        if floors_counter % 2 != 0 and floors_counter < floors:
            print(f"A{floors_counter}{rooms_counter}",end=' ')
        elif floors_counter % 2 == 0 and floors_counter < floors:
            print(f"O{floors_counter}{rooms_counter}",end=' ')
        elif floors_counter == floors:
            print(f"L{floors_counter}{rooms_counter}", end=' ')

    print("")

