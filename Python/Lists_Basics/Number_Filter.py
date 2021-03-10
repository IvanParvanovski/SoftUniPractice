numbers = int(input())
even = list()
odd = list()
negative = list()
positive = list()

for number_counter in range(numbers):
    num = int(input())
    if num >= 0:
        positive.append(num)
    else:
        negative.append(num)
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
command = input()
if command.lower() == "positive":
    print(positive)
elif command.lower() == "negative":
    print(negative)
elif command.lower() == "even":
    print(even)
else:
    print(odd)