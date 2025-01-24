class NewArray:

    def __init__(self, size):
        self.size = size
        self.array = [None] * size


    def __len__(self):
        return len(self.array)


    def __setitem__(self, key, value):
        if not 0 <= key < len(self.array):
            raise IndexError("index out of bound error")
        self.array[key] = value

    def __getitem__(self, key):
        if 0 <= key < self.size:
            return self.array[key]
        raise IndexError("index out of bound error")


    def __str__(self):
        return str(self.array)


    def is_empty(self):
        return self.size == 0


    def clear(self):
        self.array = [None] * self.size
        self.size = 0


    def __eq__(self, other):
        if not isinstance(other, NewArray):
            return NotImplemented
        if len(self.array) != len(other.array):
            return False
        for i in range(len(self.array)):
            if self.array[i] != other.array[i]:
                return False
        return True



array = NewArray(4)
new_array = NewArray(4)
array[1] = 3
print(array[1])