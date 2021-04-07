def has_car(salary,
            expenses,
            salary_rise,
            car_price,
            months_given):
    counter = 0
    saved_money = 0

    while True:
        if counter > months_given:
            return False

        if saved_money >= car_price:
            return True

        saved_money += salary
        saved_money -= expenses

        salary += salary_rise
        counter += 1


salary = float(input())
expenses = float(input())
salary_rise = float(input())
car_price = float(input())
months_given = int(input())

expression = has_car(salary,
                     expenses,
                     salary_rise,
                     car_price,
                     months_given)

print('Have a nice ride!' if expression else 'Work harder!')
