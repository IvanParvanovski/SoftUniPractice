import sys
from collections import defaultdict, deque


class CombinationWithLeastMoney:
    def __init__(self,
                 company_name='',
                 combination=()):

        self.company_name = company_name
        self.combination = combination
        self.value = sys.maxsize

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return (f'CombinationWithLeastMoney('
                f'{self.company_name!r}, {self.combination!r}, {self.value!r})')


class LeftCompany:
    def __init__(self,
                 owner_name,
                 number):

        self.owner_name = owner_name
        self.number = number

    def __str__(self):
        return f'{self.owner_name}{self.number}'

    def __repr__(self):
        return (f'LeftCompany('
                f'{self.owner_name!r}, {self.number!r})')


def generate_businesses(businesses_count):
    businesses = defaultdict(list)
    for _ in range(businesses_count):
        data = input().split(' -> ')
        owner_name = data[0]

        try:
            net_worth = tuple(map(int, data[1].split(', ')))
        except ValueError:
            net_worth = tuple()

        businesses[owner_name].extend(net_worth)

    return businesses


businesses_count = int(input())
businesses = generate_businesses(businesses_count)


left_companies = deque()
combinations = defaultdict(list)

combination_with_least_money = CombinationWithLeastMoney()
for business, business_companies in businesses.items():
    business_companies_sorted = deque(sorted(business_companies))

    while business_companies_sorted:
        biggest_side = business_companies_sorted.pop()
        try:
            smallest_side = business_companies_sorted.popleft()

            difference = biggest_side - smallest_side
            combination = str(biggest_side), str(smallest_side)

            if difference < combination_with_least_money.value:
                combination_with_least_money.company_name = business
                combination_with_least_money.combination = combination
                combination_with_least_money.value = difference

            combinations[business].append(combination)

        except IndexError:
            left_companies.append(LeftCompany(business, biggest_side))

if len(left_companies) == 1:
    combinations[combination_with_least_money.company_name].remove(combination_with_least_money.combination)
    for part in combination_with_least_money.combination:
        left_companies.append(LeftCompany(combination_with_least_money.company_name, int(part)))

total = 0
for owner_name, owner_combinations in combinations.items():
    result = f'{owner_name} | '
    if not owner_combinations:
        result += 'none'
    else:
        sorted_owner_combinations = sorted(owner_combinations, key=lambda x: abs(int(x[0]) - int(x[1])))
        for owner_combination in owner_combinations:
            total += int(owner_combination[0]) - int(owner_combination[1])
            result += ' <-> '.join(owner_combination) + ', '
    print(result[:-2:])

if left_companies:
    left_companies_sorted = deque(sorted(left_companies, key=lambda x: x.number))
    smallest_company = left_companies_sorted.popleft()
    while left_companies_sorted:
        other_company = left_companies_sorted.pop()
        print(f'{smallest_company} <-> {other_company}')

print(total)
