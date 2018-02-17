from DataStructures.Node import Node


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

    def size(self):
        temp_stack = Stack()
        count = 0
        while self.top:
            temp_stack.push(self.pop())
            count+=1

        while temp_stack.top:
            self.push(temp_stack.pop())

        return count

    def isEmpty(self):
        return self.top == None