from collections import defaultdict

my_dict = defaultdict(list)
print(my_dict)

my_dict['dogs'].append('Husky')
my_dict['dogs'].append('Labrador')

print(my_dict)

my_dict['cats'].append('Yellow-Cat')
my_dict['cats'].append('Blue-Cat')

print(my_dict)
print(my_dict['dogs'])
print(my_dict['cats'])
