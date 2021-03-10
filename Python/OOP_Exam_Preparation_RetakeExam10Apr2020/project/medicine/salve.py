from project.medicine.medicine import Medicine


class Salve(Medicine):
    def __init__(self):
        health_increase = 50
        super().__init__(health_increase)
