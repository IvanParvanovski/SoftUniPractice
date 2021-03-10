people = int(input())
presents = int(input())

money_present_counter = 0
electric_present_counter = 0
vaucheri_present_counter = 0
others_present_counter = 0

for counter in range(presents):
    type_present = input()

    if type_present == "A":
        money_present_counter += 1
    elif type_present == "B":
        electric_present_counter += 1
    elif type_present == "V":
        vaucheri_present_counter += 1
    elif type_present == "G":
        others_present_counter += 1
A_group_procent = money_present_counter / presents * 100
B_group_procent = electric_present_counter / presents * 100
V_group_procent = vaucheri_present_counter / presents * 100
G_group_procent = others_present_counter / presents * 100
people_with_present = presents / people * 100

print(f"{A_group_procent:.2f}%")
print(f"{B_group_procent:.2f}%")
print(f"{V_group_procent:.2f}%")
print(f"{G_group_procent:.2f}%")
print(f"{people_with_present:.2f}%")
