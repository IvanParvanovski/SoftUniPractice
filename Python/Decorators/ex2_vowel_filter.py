def vowel_filter(function):
    vowels = ('a',
              'e',
              'i',
              'o',
              'u')

    def wrapper():
        return [letter for letter in function() if letter.lower() in vowels]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


@vowel_filter
def get_letters2():
    return ['A', 'B', 'C', 'D', 'E']

print(get_letters())
print(get_letters2())
