class Party:
    def __init__(self):
        self.guests = list()

    def add_guests(self, person):
        self.guests.append(person)

    def get_summary(self):
        guests_names = ", ".join(list(guest.name for guest in self.guests))
        output = f"Going: {guests_names}\nTotal: {len(self.guests)}"
        return output


class Person:
    def __init__(self, name):
        self.name = name


party = Party()
command = input()

while command != "End":
    person_name = command
    person = Person(person_name)
    party.add_guests(person)
    command = input()

print(party.get_summary())