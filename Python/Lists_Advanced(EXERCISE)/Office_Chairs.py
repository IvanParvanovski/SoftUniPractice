

# for counter in range(rooms):
#     room_chairs = input().split()
#     free_places = len(room_chairs[0])
#     taken_places = abs(int(room_chairs[1]))
#
#     chairs = taken_places - free_places
#
#     if chairs <= 0:
#         free_chairs_total += abs(chairs)
#     else:
#         need_chairs_total += chairs
#         if chairs > 0:
#             print(f"{abs(chairs)} more chairs needed in room {counter + 1}")
#
# if free_chairs_total - need_chairs_total > need_chairs_total:

rooms = int(input())
free_chairs_total = 0

is_valid = True
for counter in range(rooms):
    data = input().split()
    room_chairs = len(data[0])
    taken_chairs = int(data[1])

    free_place = room_chairs - taken_chairs

    if free_place >= 0:
        free_chairs_total += free_place
    else:
        is_valid = False
        print(f"{abs(free_place)} more chairs needed in room {counter + 1}")
if is_valid:
    print(f"Game On, {free_chairs_total} free chairs left")
