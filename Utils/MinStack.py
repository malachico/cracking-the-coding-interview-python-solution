from Utils.Stack import Stack


class MinStack:
    def __init__(self):
        self.normal = Stack()
        self.mins = Stack()

    def isEmpty(self):
        return self.normal.top == None

    def peek(self):
        if self.isEmpty():
            "print empty... cant peek"
            return None

        num = self.mins.pop().data
        self.mins.push(num)
        return num

    def push(self, num):
        if self.isEmpty():
            self.normal.push(num)
            self.mins.push(num)
            return

        if self.peek() >= num:
            self.mins.push(num)

        self.normal.push(num)

    def pop(self):
        value = self.normal.pop()
        if value == self.peek():
            self.mins.pop()

        return value

    def get_min(self):
        return self.peek()