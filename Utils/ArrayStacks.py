from array import array

from Utils.StackNode import StackNode

ARRAY_SIZE = 30

class ArrayStacks:
    def __init__(self):
        self.arr = [None]*ARRAY_SIZE
        self.stacksPointers = [-1, -1, -1]
        self.currentIndex = 0

    def push(self, data, stackNum):
        if None not in self.arr:
            print "Array is full."
            return

        # Get stack pointer
        stackPointer = self.stacksPointers[stackNum]

        # Create stack node
        stackNode = StackNode(value=data, prev=stackPointer)

        # Put stack node in the current index
        self.arr.insert(self.currentIndex, stackNode)

        # update stack pointer
        self.stacksPointers[stackNum] = self.currentIndex

        # find next current index
        self.currentIndex=self.arr.index(None)


    def pop(self, stackNum):
        # Get stack pointer
        stackPointer = self.stacksPointers[stackNum]

        if stackPointer == -1:
            print "stack is empty"
            return

        # Get node in stack pointer
        stackNode = self.arr[stackPointer]

        # Update stack pointer
        self.stacksPointers[stackPointer] = stackNode.prev

        # Remove object from array
        self.arr.remove(stackNode)

        # Return value
        return stackNode.value


    def to_string(self):
        s = ""
        for obj in self.arr:
            s += str(obj.prev) + " "
            s += str(obj.value)
            s += " | "

        print s

