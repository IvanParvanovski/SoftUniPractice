from collections import namedtuple

# person1 = {
#     'hair': 'brown',
#     'eyes': 'blue',
#     'body': 'strong',
# }
#
# person2 = {
#     'hair': 'brown',
#     'eyes': 'blue',
#     'body': 'strong',
# }

accepted_hair_colors = ('brown',
                        'yellow',
                        'red')


assert input() in accepted_hair_colors, 'Invalid Hair Color!'

Person = namedtuple('Person', [
    'hair',
    'eyes',
    'body',
])

person1 = Person('brown', 'blue', 'strong')
person2 = Person('blond', 'green', 'weak')


