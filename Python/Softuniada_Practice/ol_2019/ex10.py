from types import MappingProxyType


class Search:
    def __init__(self, field):
        self.field = field

    def get_channel_with_least_empty(self, determine, determine_opposite):
        pass
        # for

def get_channels(channels_c):
    for _ in range(channels_c):
        yield tuple(int(x) for x in input().split())


def generate_field(channels_values, field_length):
    current_field = list()

    for channel in channels_values:
        roots = channel[0]
        fungus = channel[1]

        current_field.append(['T'] * roots +
                             ['-'] * (field_length - (fungus + roots)) +
                             ['F'] * fungus)

    return current_field


channels_count = int(input())
channels = tuple(get_channels(channels_count))
field_radius = int(input())

field = generate_field(channels, field_radius)

for f in field:
    print(f)

day_or_night = MappingProxyType({
    1: 'day',
    2: 'night',
})

day_or_night_index = 1
while True:

    if day_or_night_index == 3:
        day_or_night_index = 1



    day_or_night_index += 1
