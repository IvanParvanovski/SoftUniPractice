def dog(type_):
    def food(current_food):
        # type_ = 'Husky'
        return '%s food is: %s' % (type_, current_food)

    def fur(current_fur):
        # type_ = 'Husky'
        return '%s fur is: %s' % (type_, current_fur)

    return (
        food,
        fur,
    )


husky = dog('Husky')
print(husky[0](current_food='Sausage'))
print(husky[1](current_fur='White'))
