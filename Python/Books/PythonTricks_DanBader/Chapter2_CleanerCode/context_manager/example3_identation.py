class Indenter(object):
    def __init__(self):
        self.level = 0

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1

    def print(self, text):
        print(self.level * '\t' + text)


with Indenter() as indent:
    indent.print('hi!')
    with indent:
        indent.print('hi')
        with indent:
            indent.print('bonjour')
    indent.print('hey')
