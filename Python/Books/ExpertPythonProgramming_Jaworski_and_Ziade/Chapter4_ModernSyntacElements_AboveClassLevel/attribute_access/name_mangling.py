class MyClass:
    __secret_value = 1


instance_of = MyClass()
print(dir(MyClass))

print(instance_of.__secret_value)
