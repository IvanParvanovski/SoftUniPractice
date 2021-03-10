class Trainer:
    auto_increment = 1

    def __init__(
            self,
            name: str):

        self.name = name
        self.id = Trainer.auto_increment
        Trainer.auto_increment += 1

    @staticmethod
    def get_next_id():
        return Trainer.auto_increment

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"
