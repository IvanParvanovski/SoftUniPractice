class AlwaysEquals:
    def __eq__(self, other):
        return True

    def __hash__(self):
        return id(self)

#
# print(AlwaysEquals() == AlwaysEquals())
# print(AlwaysEquals() == 42)
# print(AlwaysEquals() == 'watt?')

objects = [
    AlwaysEquals(),
    AlwaysEquals(),
    AlwaysEquals(),
]

print([hash(obj) for obj in objects])

print({AlwaysEquals(): 'yes', AlwaysEquals(): 'no'})

