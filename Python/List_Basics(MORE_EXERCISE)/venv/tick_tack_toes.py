first_line = input().split()
second_line = input().split()
third_line = input().split()


# def first_player_calculations():
first_player_counter = 0
second_player_counter = 0

for element in first_line:
    if element == "1":
        first_player_counter += 1
    elif element == "2":
        second_player_counter += 1

for element in second_line:
    if element == "1":
        first_player_counter += 1
    elif element == "2":
        second_player_counter += 1

for element in third_line:
    if element == "1":
        first_player_counter += 1
    elif element == "2":
        second_player_counter += 1

# return first_player_counter, second_player_counter


#first_player_counter, second_player_counter = first_player_calculations()

if first_player_counter == second_player_counter:
    print("Draw!")
elif first_player_counter > second_player_counter:
    print("First player won")
elif second_player_counter > first_player_counter:
    print("Second player won")
