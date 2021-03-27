gifts = input().split()

if not gifts:
    raise ValueError('No gifts')

while True:
    user_input = input()
    if user_input == 'No Money':
        break

    data = user_input.split()
    command = data[0]
    gift = data[1]

    if command == 'OutOfStock':
        gifts = [c_gift for c_gift in gifts if c_gift != gift]

    elif command == 'Required':
        index = int(data[2])
        assert -1 < index < len(gift), 'Invalid Index!'
        gifts[index] = gift

    elif command == 'JustInCase':
        gifts[-1] = gift

print(' '.join(gifts))
