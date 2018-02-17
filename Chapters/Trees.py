import unittest

from DataStructures.BSTree import BSTree


def check_balanced(node, height, ):
    if not node:
        return


def get_rightest_height(t):
    counter = 0
    current = t

    while current.right:
        counter += 1
        current = current.right

    return counter


def is_balanced_helper(height, node, current=0):
    if node is None:
        return -2 < current - height < 2

    return is_balanced_helper(height, node.right, current+1) \
           and is_balanced_helper(height, node.left, current+1)

def is_balanced(t, current_height=0):

    height = get_rightest_height(t)

    return is_balanced_helper(height, t)

class TreesTests(unittest.TestCase):
    def test0(self):
        t = BSTree(3)
        t.insert(2)
        t.insert(4)
        t.insert(4)

        a = self.assertTrue(is_balanced(t.root))
        t.insert(5)
        t.insert(6)
        t.insert(7)

        self.assertFalse(is_balanced(t.root))