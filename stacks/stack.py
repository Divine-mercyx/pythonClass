class Stack:

    def __init__(self, size):
        self.size = size
        self.data = []


    def is_empty(self):
        return len(self.data) == 0


    def get_size(self):
        return self.size


    def peek(self):
        if not self.is_empty(): return self.data[-1]
        else: return None


    def pop(self):
        if not self.is_empty(): return self.data.pop()
        else: return None


    def push(self, value):
        if self.size != len(self.data): self.data.append(value)

