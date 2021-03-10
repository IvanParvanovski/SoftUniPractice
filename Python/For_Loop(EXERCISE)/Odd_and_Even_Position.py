import sys

numbers_count = int(input())

oddSum = 0

odd_minNumber = sys.maxsize
odd_maxNumber = -sys.maxsize

evenSum = 0
even_minNumber = sys.maxsize
even_maxNumber = -sys.maxsize

for counter in range(1,numbers_count + 1):
    numbers = float(input())

    if counter % 2 == 0:

        if numbers > even_maxNumber:
            even_maxNumber = numbers

        if numbers < even_minNumber:
            even_minNumber = numbers

        evenSum += numbers

    else:

        if numbers > odd_maxNumber:
            odd_maxNumber = numbers

        if numbers < odd_minNumber:
            odd_minNumber = numbers

        oddSum += numbers
#Odd

print(f"OddSum={oddSum:.2f},")

if odd_minNumber == sys.maxsize:
    print(f"OddMin=No,")
else:
    print(f"OddMin={odd_minNumber:.2f},")

if odd_maxNumber == -sys.maxsize:
    print("OddMax=No,")
else:
    print(f"OddMax={odd_maxNumber:.2f},")

#Even
print(f"EvenSum={evenSum:.2f},")

if even_minNumber == sys.maxsize:
    print(f"EvenMin=No,")
else:
    print(f"EvenMin={even_minNumber:.2f},")

if even_maxNumber == -sys.maxsize:
    print("EvenMax=No")
else:
    print(f"EvenMax={even_maxNumber:.2f}")
