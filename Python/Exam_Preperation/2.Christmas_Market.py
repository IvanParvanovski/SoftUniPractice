from math import floor
need_sum = float(input())
fentasi_books = int(input())
horror_books = int(input())
romantic_books = int(input())
diff_procent = 0
procent = 0

fentasi_sum = fentasi_books * 14.90
horror_sum = horror_books * 9.80
romantic_sum = romantic_books * 4.30

sum = fentasi_sum + horror_sum + romantic_sum

sum_with_DDS = sum - (20/100 * sum)

if sum_with_DDS >= need_sum:
    diff = sum_with_DDS - need_sum
    diff_procent = diff - (10 / 100 * diff)

    procent = 10 / 100 * diff
    procent = floor(procent)
    sum_with_DDS -= procent

if sum_with_DDS >= need_sum:
    print(f"{sum_with_DDS:.2f} leva donated.")
    print(f"Sellers will receive {procent} leva.")
else:
    diff = need_sum - sum_with_DDS
    print(f"{diff:.2f} money needed.")