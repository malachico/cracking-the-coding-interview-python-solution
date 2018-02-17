import unittest

from DataStructures.ArrayStacks import ArrayStacks


# tests
from DataStructures.MinStack import MinStack
from DataStructures.PileStacks import PileStacks
from DataStructures.Stack import Stack


class StacksAndQueuesTest(unittest.TestCase):
    def test0(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.size(), 1)
        stack.push(2)
        stack.push(2)
        stack.push(2)
        stack.push(2)
        self.assertEqual(stack.size(), 5)
        stack.pop()
        self.assertEqual(stack.size(), 4)

    def test1(self):
        stacks = ArrayStacks()

        stacks.push('data0', 0)
        stacks.push('data1', 1)

        self.assertEqual(stacks.pop(1), "data1")
        self.assertEqual(stacks.pop(0), "data0")

        stacks.push('data2', 0)
        stacks.push('data3', 0)
        stacks.push('data4', 0)

        self.assertEqual(stacks.pop(0), 'data4')

    def test2(self):
        minStack = MinStack()
        minStack.push(1)
        minStack.push(2)
        print minStack.get_min()


    def test3(self):
        pileStacks = PileStacks()

        pileStacks.push(1)
        pileStacks.push(3)

        self.assertEqual(pileStacks.pop(), 3)

        pileStacks.push(2)
        pileStacks.push(3)

        pileStacks.push(4)

        self.assertEqual(len(pileStacks.arr), 2)
        self.assertEqual(pileStacks.pop(), 4)
        self.assertEqual(len(pileStacks.arr), 1)


