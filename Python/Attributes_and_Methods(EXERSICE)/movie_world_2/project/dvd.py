class DVD:
    def __init__(self,
                 name: str,
                 id: int,
                 creation_year: int,
                 creation_month: str,
                 age_restriction: int):

        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @staticmethod
    def find_month_name(month_num):
        months = {
            1: "January",
            2: "February",
            3: "March",
            4: "April",
            5: "May",
            6: "June",
            7: "July",
            8: "August",
            9: "September",
            10: "October",
            11: "November",
            12: "December"
        }

        return months[month_num]

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        splited_date = date.split('.')
        month_num = int(splited_date[1])

        month = DVD.find_month_name(month_num)
        year = int(splited_date[2])

        return cls(name, id, year, month, age_restriction)

    def rent_message(self):
        return "rented" if self.is_rented else "not rented"

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year})" \
               f" has age restriction {self.age_restriction}. Status: {self.rent_message()}"
