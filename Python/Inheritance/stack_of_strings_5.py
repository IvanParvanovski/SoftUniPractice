class Stack:
    def __init__(self):
        self.data = list()

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __repr__(self):
        return f"[{', '.join(self.data[::-1])}]"


st = Stack()
st.push("hi1")
st.push("hi2")
st.push("hi3")
st.push("hi4")
print(st)
