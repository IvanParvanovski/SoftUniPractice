class Room:
    def __init__(self, number: int, capacity: int):
        self.number = number
        self.capacity = capacity
        self.guests = 0
        self.is_taken = False

    def can_be_freed(self):
        return self.is_taken

    def can_be_taken(self, people):
        return not self.is_taken and self.capacity >= people

    def take_room(self, people):
        if not self.can_be_taken(people):
            return f"Room number {self.number} cannot be taken"

        self.is_taken = True
        self.guests = people

    def free_room(self):
        if not self.can_be_freed():
            return f"Room number {self.number} is not taken"

        self.is_taken = False
        self.guests = 0

