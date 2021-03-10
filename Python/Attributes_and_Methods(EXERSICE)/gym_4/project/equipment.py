class Equipment:
    auto_increment = 1

    def __init__(
            self,
            name: str):

        self.name = name
        self.id = Equipment.auto_increment
        Equipment.auto_increment += 1

    @staticmethod
    def get_next_id():
        return Equipment.auto_increment

    def __repr__(self):
        return F"Equipment <{self.id}> {self.name}"
