def is_prime(n):
    # Corner case
    if n <= 1:
        return False

    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False

    return True


first_number = int(input())
second_number = int(input())
result = list()

for n in range(first_number, second_number + 1):
    if is_prime(n):
        result.append(n)

print(' '.join(map(str, result)))
print(f'The total number of prime numbers between {first_number} to {second_number} is {len(result)}')


