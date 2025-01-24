class Set:

    def __init__(self):
        self.array = []


    def is_empty(self):
        return len(self.array) == 0


    def index_of(self, value):
        return self.array.index(value)


    def add(self, value):
        if value not in self.array: self.array.append(value)


    def contains(self, value):
        if value in self.array: return True
        return False


    def size(self):
        return len(self.array)


    def remove(self, value):
        if value in self.array: self.array.remove(value)


    def __str__(self):
        return str(set(self.array))


    def retain_all(self, lists):
        self.array = []
        for i in lists: self.array.append(i)

