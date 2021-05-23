substrings = ['These ',
              'are ',
              'strings ',
              'to ',
              'concatenate.',]


# Bad practice

s = ''
for string in substrings:
    s += string

print(s)
print()

# Good practice

print(''.join(substrings))
print(str.join('', substrings))

# Constant folding
print('a' + 'b' + 'c')
