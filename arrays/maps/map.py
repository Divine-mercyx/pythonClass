from sets.set import Set

class Map:

    def __init__(self):
        self.keys = Set()
        self.values = []
        self.size = 0


    def is_empty(self):
        self.keys.is_empty()


    def put(self, key, value):
        self.keys.add(key)
        self.values.append(value)
        self.size += 1


    def size(self):
        return self.size


    def get(self, key):
        if self.keys.contains(key):
            index = self.keys.index_of(key)
            return self.values[index]


    def contains_key(self, key):
        return key in self.keys


    def contains_value(self, value):
        return value in self.values