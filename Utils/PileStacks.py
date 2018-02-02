from Utils.Stack import Stack
MAX_SIZE = 3

class PileStacks:
    def __init__(self):
        self.arr = []

    def isEmpty(self):
        return len(self.arr) == 0

    def push(self, value):
        if self.isEmpty():
            self.arr.append(Stack())

        currentStack = self.arr[len(self.arr) -1]

        if currentStack.size() >= MAX_SIZE:
            self.arr.append(Stack())

        currentStack = self.arr[len(self.arr) - 1]

        currentStack.push(value)

    def pop(self):
        if self.isEmpty():
            print "empty.. returning"
            return

        currentStack = self.arr[len(self.arr) - 1]

        value = currentStack.pop().data

        if currentStack.isEmpty():
            self.arr.remove(currentStack)

        return value
