kv_meters = float(input())
first_sum = kv_meters * 7.61
discount = 18/100 * first_sum
full_sum = first_sum - discount
print(f"The final price is: {full_sum:.2f} lv.")
print(f"The discount is: {discount:.2f} lv.")