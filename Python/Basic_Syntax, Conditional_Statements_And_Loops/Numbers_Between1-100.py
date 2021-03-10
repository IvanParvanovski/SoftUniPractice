number = 0
min_Criteria = 1
max_Criteria = 100

while number < min_Criteria or number > max_Criteria:
    number = float(input("Please enter number between 1 and 100: "))

print(f"The number {number} is between 1 and 100")