age = float(input())
gender = input()
type = ""

if age >= 16 and gender == "m":
    type = "Mr."
if age < 16 and gender == "m":
    type = "Master"
if age >= 16 and gender == "f":
    type = "Ms."
if age < 16 and gender == "f":
    type = "Miss"

print(type)
