final_type = input()
ticket_type = input()
ticket_count = int(input())
photo_with_trophy = input()
total = 0

if final_type == "Quarter final":
    if ticket_type == "Standard":
        total = ticket_count * 55.50
    elif ticket_type == "Premium":
        total = ticket_count * 105.20
    elif ticket_type == "VIP":
        total = ticket_count * 118.90

elif final_type == "Semi final":
    if ticket_type == "Standard":
        total = ticket_count * 75.88
    elif ticket_type == "Premium":
        total = ticket_count * 125.22
    elif ticket_type == "VIP":
        total = ticket_count * 300.40

elif final_type == "Final":
    if ticket_type == "Standard":
        total = ticket_count * 110.10
    elif ticket_type == "Premium":
        total = ticket_count * 160.66
    elif ticket_type == "VIP":
        total = ticket_count * 400

b = False
if total > 4000:
    total *= 0.75
    b = True

elif total > 2500:
    total *= 0.9

if photo_with_trophy == "Y":
    if not b:
        total += 40 * ticket_count
    print(f'{total:.2f}')


elif photo_with_trophy == "N":
    print(f'{total:.2f}')