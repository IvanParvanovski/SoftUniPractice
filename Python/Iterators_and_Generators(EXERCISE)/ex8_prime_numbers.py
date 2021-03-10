def get_primes(numbers):
    for num in numbers:
        is_prime = True

        if num == 1 or num == 0:
            is_prime = False

        for n in range(2, num):
            if num % n == 0:
                is_prime = False

        if is_prime:
            yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
