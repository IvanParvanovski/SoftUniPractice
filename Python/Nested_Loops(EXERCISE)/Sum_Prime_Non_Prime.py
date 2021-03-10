text = ""
sum_non_prime = 0
sum_prime = 0
while text != "stop":
    text = input()
    if text == "stop":
        break
    current_num = int(text)
    if current_num < 0:
        print("Number is negative.")
        text = input()
        continue