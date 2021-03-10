from collections import defaultdict
metals_dict = defaultdict(int)

command = input()
while command != "stop":
    quantity = int(input())
    metals_dict[command] += quantity
    command = input()

for element in metals_dict:
    print(f"{element} -> {int(metals_dict[element])}")