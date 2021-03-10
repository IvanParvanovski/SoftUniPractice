# class Weapon:
#     def __init__(self, bullet):
#         self.bullets = bullet
#         self.message = ""
#
#     def shoot(self):
#         if self.bullets > 0:
#             self.bullets -= 1
#             return "shooting..."
#         else:
#             return "no bullets left"
#
#     def __repr__(self):
#         return f"Remaining bullets: {self.bullets}"
#
#
# weapon = Weapon(5)
# weapon.shoot()
# weapon.shoot()
# weapon.shoot()
# weapon.shoot()
# weapon.shoot()
# weapon.shoot()
# print(weapon)


local_list = ["Hello", "World", "Soft", "Uni"]

for element in local_list:
    print(element)
