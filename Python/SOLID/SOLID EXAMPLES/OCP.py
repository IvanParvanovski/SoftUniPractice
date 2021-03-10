class StudentTaxes:
    def __init__(self, name, semester_tax, average_grade):
        self.name = name
        self.semester_tax = semester_tax
        self.average_grade = average_grade

    def get_discount(self):
        if self.average_grade > 5:
            return self.semester_tax * 0.4


class AdditionalDiscount(StudentTaxes):
    def get_discount(self):
        super().get_discount()
        if 4 < self.average_grade <= 5:
            return self.semester_tax * 0.2
