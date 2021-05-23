def full_loop():
    i = 0
    for element in ['one', 'two', 'three']:
        print(i, element)
        i += 1
    print()


full_loop()

for i, element in enumerate(['one', 'two', 'three']):
    print(i, element)
