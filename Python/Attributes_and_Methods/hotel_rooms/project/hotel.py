class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = list()
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def get_room_by_number(self, room_number):
        return [room for room in self.rooms if room.number == room_number][0]

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = self.get_room_by_number(room_number)
        result = room.take_room(people)
        if result:
            return result

        self.guests += people

    def free_room(self, room_number):
        room = self.get_room_by_number(room_number)
        guests_to_remove = room.guests
        result = room.free_room(room)
        if result:
            return result

        self.guests -= guests_to_remove

    def print_status(self):
        free_rooms = list()
        taken_rooms = list()

        for room in self.rooms:
            if room.is_taken:
                taken_rooms.append(str(room.number))
            else:
                free_rooms.append(str(room.number))

        result = f"Hotel {self.name} has {self.guests} total guests\n" \
                 f"Free rooms: {', '.join(free_rooms)}\n" \
                 f"Taken rooms: {', '.join(taken_rooms)}"

        print(result)
