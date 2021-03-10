wiski_Price = float(input())
beer = float(input())
wine = float(input())
rakiq = float(input())
wiski = float(input())

rakiq_Price = wiski_Price/2
wine_Price = rakiq_Price - (40/100) * rakiq_Price
beer_Price = rakiq_Price - (80/100) * rakiq_Price

beer_sum = beer * beer_Price
wine_sum = wine * wine_Price
rakiq_sum = rakiq_Price * rakiq
wiski_sum = wiski * wiski_Price

full_sum = beer_sum + wine_sum + rakiq_sum + wiski_sum

print(f"{full_sum:.2f}")