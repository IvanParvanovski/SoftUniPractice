import sys
winner_name = ""
winner_score = -sys.maxsize

score = 0
name = input()
len_name = len(name)

while name != "STOP":

    for symbol in range(len_name):
        k = ord(name[symbol])
        score += k

    if score > winner_score:
        winner_score = score
        winner_name = name

    name = input()
    len_name = len(name)
    score = 0

print(f"Winner is {winner_name} - {winner_score}!")
