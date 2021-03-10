# Ako имаме университет, който има книга с правила
# И всеки ден добавяме ново правило
# Как трябва да стане прогрмата спрямо втория принцип на SOLID?


class University:
    def __init__(self, name):
        self.name = name
        self.book_of_rules = list()

    def rules(self, a):
        if a == 1:
            msg = "Main Rule - 1"
            self.book_of_rules.append(msg)
            return msg

        elif a == 2:
            msg = "Main Rule - 2"
            self.book_of_rules.append(msg)
            return msg

        elif a == 3:
            msg = "Main Rule - 3"
            self.book_of_rules.append(msg)
            return msg


# Добавено на - 24/7/2020
class AdditionalSecondaryRule1(University):
    def rules(self, a):
        super().rules(a)

        if a == 4:
            msg = "Secondary Rule - 1"
            self.book_of_rules.append(msg)
            return msg


# Добавено на - 25/7/2020
class AdditionalSecondaryRule2(AdditionalSecondaryRule1):
    def rules(self, a):
        super().rules(a)

        if a == 5:
            msg = "Secondary Rule - 2"
            self.book_of_rules.append(msg)
            return msg


# Добавено на - 26/7/2020
class AdditionalSecondaryRule3(AdditionalSecondaryRule2):
    def rules(self, a):
        super().rules(a)

        if a == 6:
            msg = "Secondary Rule - 1"
            self.book_of_rules.append(msg)
            return msg


# Добавено на - 27/7/2020
class AdditionalSecondaryRule4(AdditionalSecondaryRule3):
    def rules(self, a):
        super().rules(a)

        if a == 7:
            msg = "Secondary Rule - 2"
            self.book_of_rules.append(msg)
            return msg

# ...
