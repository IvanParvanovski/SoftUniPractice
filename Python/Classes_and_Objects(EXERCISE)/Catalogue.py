class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = list()
        self.list_with_that_letter = list()

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, first_letter):
        self.first_letter = first_letter
        return list(element for element in self.products if element[0] == self.first_letter)

    def __repr__(self):
        self.message = f"Items in the {self.name} catalogue:\n"
        self.message += "\n".join(sorted(self.products))
        return self.message

catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
