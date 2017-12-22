from Utils.Node import Node


class Queue:
    def __init__(self, *data):
        self.first = None
        self.last = None

        for d in data:
            self.enqueue(d)

    def enqueue(self, data):
        n = Node(data)
        if self.count() == 0:
            self.first = self.last = n
            return

        self.last.next = n
        self.last = n

    def dequeue(self):
        if self.count() == 0:
            return
        d = self.first
        self.first = self.first.next

    def count(self):
        counter = 0
        i = self.last

        while i:
            counter+=1
            i = i.next

        return counter


