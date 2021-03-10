from fibonacci_sequence import create_sequence


def locate_num(num, sequence):
    if num in sequence:
        return f"The number - {num} is at index {sequence.index(num)}"
    return f"The number {num} is not in the sequence"


sequence = list()

while True:
    raw_input = input().split()
    command = raw_input[0]

    if command == "Stop":
        break

    elif command == "Create":
        num = int(raw_input[2])
        sequence = create_sequence(num)
        print(' '.join(sequence))

    elif command == "Locate":
        num = raw_input[1]
        print(locate_num(num, sequence))
