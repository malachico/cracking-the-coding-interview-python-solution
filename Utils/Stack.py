from Utils.Node import Node


class Stack:

    def __init__(self, *data):
        self.top = None

        for d in data:
            self.push(d)

    def push(self, data):
        n = Node(data)
        n.next= self.top
        self.top = n

    def pop(self):
        if not self.top:
            return

        data = self.top
        self.top = data.next
        return data

