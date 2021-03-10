type_film = input()
rows = int(input())
columns = int(input())
ticket_price = 0

if type_film == "Premiere":
    ticket_price = 12.00

if type_film == "Normal":
    ticket_price = 7.50

if type_film == "Discount":
    ticket_price = 5.00

seats = rows * columns
sum = ticket_price * seats

print(f"{sum:.2f} leva")
