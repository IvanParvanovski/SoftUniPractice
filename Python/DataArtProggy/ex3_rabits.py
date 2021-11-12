import time


def calculate_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Runtime of the func is: {end - start}')

        return result
    return wrapper


# O(n) n = len(cages_)
@calculate_time
def is_valid(rabbits_count_, cages_):
    # total = 0
    for i in range(len(cages)):
        if i == len(cages_) - 1:
            cages_[i] = rabbits_count_
        else:
            current_rabbits = i + 1
            # total += current_rabbits
            cages_[i] = current_rabbits
            rabbits_count_ -= current_rabbits

        if rabbits_count_ <= 0:
            return 'invalid'

    last_value = cages_.pop()

    if last_value in cages_:
        return 'invalid'

    return 'valid'


print('Cages, Rabbits')
cages_count, rabbits_count = map(int, input().split())

cages = [0] * cages_count
print(is_valid(rabbits_count, cages))

# 5 20 -> valid
# 5 3 -> invalid
# 1 1 -> valid
# 500 20000 -> invalid
