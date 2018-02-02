import unittest

from Utils.ArrayStacks import ArrayStacks


# tests
from Utils.MinStack import MinStack


class StacksAndQueuesTest(unittest.TestCase):
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
