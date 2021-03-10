month = input()
night_times = int(input())

studio_sum = 0
apartment_sum = 0

if month == "May" or month == "October":
    studio_sum = 50 * night_times
    apartment_sum = 65 * night_times

    if night_times > 7 and night_times < 14:
        studio_sum -= 5 / 100 * studio_sum
    if night_times > 14:
        studio_sum -= 30 / 100 * studio_sum
        apartment_sum -= 10 / 100 * apartment_sum

if month == "June" or month == "September":
    studio_sum = 75.20 * night_times
    apartment_sum = 68.70 * night_times

    if night_times > 14:
        studio_sum -= 20 / 100 * studio_sum
        apartment_sum -= 10 / 100 * apartment_sum

if month == "July" or month == "August":
    studio_sum = 76 * night_times
    apartment_sum = 77 * night_times

    if night_times > 14:
        apartment_sum -= 10 / 100 * apartment_sum

print(f"Apartment: {apartment_sum:.2f} lv.")
print(f"Studio: {studio_sum:.2f} lv.")