animal = input()
animal_class = ""

if animal == "dog":
    animal_class = "mammal"
elif animal == "crocodile" or animal == "tortoise" or animal == "snake":
    animal_class = "reptile"
else:
    animal_class = "unknown"

print(animal_class)