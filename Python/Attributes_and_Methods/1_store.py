from collections import defaultdict


class Store:
    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = defaultdict(int)

    @classmethod
    def from_size(cls, name: str, type: str, size: int):
        return cls(name, type, size // 2)

    def does_store_have_free_capacity(self):
        return self.capacity > 0

    def does_item_quantity_exist(self, item_name, amount):
        return self.items[item_name] >= amount

    def add_item(self, item_name: str):
        if not self.does_store_have_free_capacity():
            return "Not enough capacity in the store"

        self.items[item_name] += 1
        self.capacity -= 1
        return f"{item_name} added to the store"

    def remove_item(self, item_name: str, amount: int):
        if not self.does_item_quantity_exist(item_name, amount):
            return f"Cannot remove {amount} {item_name}"

        self.items[item_name] -= amount
        self.capacity += 1
        return f"{amount} {item_name} removed from the store"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"


first_store = Store("First store", "Fruit and Veg", 20)
second_store = Store.from_size("Second store", "Clothes", 500)

print(first_store)
print(second_store)

print(first_store.add_item("potato"))
print(second_store.add_item("jeans"))
print(first_store.remove_item("tomatoes", 1))
print(second_store.remove_item("jeans", 1))

