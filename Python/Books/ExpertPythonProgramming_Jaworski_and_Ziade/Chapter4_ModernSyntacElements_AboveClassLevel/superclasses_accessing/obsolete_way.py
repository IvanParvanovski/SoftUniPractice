class Mama:
    def says(self):
        print('do your homework')


class Sister(Mama):
    def says(self):
        Mama.says(self)
        print('and clean your bedroom')

