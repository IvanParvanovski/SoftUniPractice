vowels = {'a', 'e', 'i', 'o', 'u'}
print('e' in vowels)

letters = set('alice')
print(letters.intersection(vowels))

vowels.add('x')
print(vowels)

print(len(vowels))
