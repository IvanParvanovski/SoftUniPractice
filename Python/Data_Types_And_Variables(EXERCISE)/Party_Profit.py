companies = int(input())
days = int(input())
coins = 0

for days_counter in range(1, days + 1):

    if days_counter % 10 == 0:
        companies -= 2

    if days_counter % 15 == 0:
        companies += 5

    coins += 50 - 2 * companies

    if days_counter % 3 == 0:
        coins -= 3 * companies

    if days_counter % 5 == 0 and days_counter % 3 != 0:
        coins += 20 * companies

    if days_counter % 5 == 0 and days_counter % 3 == 0:
        coins += int(20 * companies)
        coins -= int(2 * companies)

company_total = int(coins / companies)
print(f"{companies} companions received {company_total} coins each.")