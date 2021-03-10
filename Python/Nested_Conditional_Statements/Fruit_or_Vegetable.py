item = input()
plant = ""

if item == "banana" or item == "apple" or item == "kiwi" or item == "cherry" or item == "lemon" or item == "grapes":
    plant = "fruit"
elif item == "tomato" or item == "cucumber" or item == "pepper" or item == "carrot":
    plant = "vegetable"
else:
    plant = "unknown"

print(plant)
