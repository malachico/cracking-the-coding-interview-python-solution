import unittest
import networkx

from DataStructures.BSTree import BSTree

# Q1 is balanced
from DataStructures.Stack import Stack


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
        return -1 < current - height - 1 < 1

    return is_balanced_helper(height, node.right, current+1) \
           and is_balanced_helper(height, node.left, current+1)

def is_balanced(t, current_height=0):

    height = get_rightest_height(t)

    return is_balanced_helper(height, t)

# Q2 DFS and BFS
def check_path_exists_BFS(G, u, v):
    stack = Stack()
    stack.push(u)
    G.nodes[u]['weight'] = 1

    while not stack.isEmpty():
        current = stack.pop()
        for n in G.neighbors(current.data):
            if n == v:
                return True

            if G.nodes[n]['weight'] == 0:
                stack.push(n)
                G.nodes[n]['weight'] = 1

    return False


class TreesTests(unittest.TestCase):
    def test0(self):
        t = BSTree(3)
        t.insert(2)
        t.insert(4)
        t.insert(4)
        self.assertTrue(is_balanced(t.root))
        t.insert(5)
        t.insert(6)
        t.insert(7)
        self.assertFalse(is_balanced(t.root))

    def test1(self):
        G= networkx.Graph()
        G.add_node("a", weight=0)
        G.add_node("b", weight=0)
        G.add_node("c", weight=0)
        G.add_node("d", weight=0)

        G.add_edge("a", "b")
        G.add_edge("b", "c")


        self.assertTrue(check_path_exists_BFS(G, "a", "c"))
        G.add_node("d")
        self.assertFalse(check_path_exists_BFS(G, "a", "d"))
