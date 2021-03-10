

number_of_tabels = int(input())
lenght_of_tabels = float(input())
width_of_tabels = float(input())

full_price_rectangels = number_of_tabels * (lenght_of_tabels + 0.60) * (width_of_tabels + 0.60)
full_price_squares = number_of_tabels * (lenght_of_tabels/2) * (lenght_of_tabels/2)

full_price_USD = (full_price_rectangels * 7 + full_price_squares * 9)
full_price_BGN = (full_price_rectangels * 7 + full_price_squares * 9) * 1.85


print(f"{full_price_USD:.2f} USD")
print(f"{(full_price_BGN):.2f} BGN")


