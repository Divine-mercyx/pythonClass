from node import Node

class linkedlist:
    def __init__(self):
        self.head = None


    def append(self, value):
        newHead = Node(value)
        newHead.next = self.head
        self.head = newHead


    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next


linked = linkedlist()
linked.append("boy")
linked.append("girl")
linked.append("mother")
linked.append("father")
linked.display()