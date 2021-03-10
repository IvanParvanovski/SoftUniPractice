class Glass:
    capacity = 250

    def __init__(self):
        self.content = 0

    def does_glass_have_free_space(self, ml):
        return self.content + ml < 250

    def fill(self, ml):
        if not self.does_glass_have_free_space(ml):
            return f"Cannot add {ml} ml"

        self.content += ml
        return f"Glass filled with {ml} ml"

    def empty(self):
        self.content = 0
        return "Glass is now empty"

    def info(self):
        return f"{Glass.capacity - self.content} ml left"
