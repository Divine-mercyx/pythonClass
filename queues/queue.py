from arrays.array import *

class Queue(MyArray):

    def __init__(self, size):
        super().__init__(size)


    def enqueue(self, value):
        self.put(value)


    def dequeue(self):
        return self.remove(0)

    def size(self):
        return self.length()


    def peek(self):
        return self.data[0]


    def element(self, index):
        return self.get(index)


    def is_empty(self):
        return self.is_empty()
