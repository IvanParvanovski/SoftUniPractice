city = input()
sells = float(input())
sum = 0

if city == "Sofia":

    if 0 <= sells <= 500:
        sum = 5 / 100 * sells
        print(f"{sum:.2f}")
    elif 500 < sells <= 1000:
        sum = 7 / 100 * sells
        print(f"{sum:.2f}")
    elif 1000 < sells <= 10000:
        sum = 8 / 100 * sells
        print(f"{sum:.2f}")
    elif sells > 10000:
        sum = 12 / 100 * sells
        print(f"{sum:.2f}")
    else:
        print("error")



elif city == "Varna":

    if 0 <= sells <= 500:
        sum = 4.5 / 100 * sells
        print(f"{sum:.2f}")
    elif 500 < sells <= 1000:
        sum = 7.5 / 100 * sells
        print(f"{sum:.2f}")
    elif 1000 < sells <= 10000:
        sum = 10 / 100 * sells
        print(f"{sum:.2f}")
    elif sells > 10000:
        sum = 13 / 100 * sells
        print(f"{sum:.2f}")
    else:
        print("error")


elif city == "Plovdiv":

    if 0 <= sells <= 500:
        sum = 5.5 / 100 * sells
        print(f"{sum:.2f}")
    elif 500 < sells <= 1000:
        sum = 8 / 100 * sells
        print(f"{sum:.2f}")
    elif 1000 < sells <= 10000:
        sum = 12 / 100 * sells
        print(f"{sum:.2f}")
    elif sells > 10000:
        sum = 14.5 / 100 * sells
        print(f"{sum:.2f}")
    else:
        print("error")

else:
    print("error")



