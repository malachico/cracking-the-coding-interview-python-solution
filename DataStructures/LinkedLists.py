import unittest

from Utils.Node import Node


def remove_duplicate_nodes(head):
    if head is None:
        return head

    current = head.next

    while current is not None:
        back = head
        if back.data == head.data:
            head.delete_node(back.data)



# tests
class MyTest(unittest.TestCase):
    def test1(self):
        head = Node(1)

        head.append_to_tail(2)
        head.append_to_tail(3)
        head.append_to_tail(4)

        head.to_string()
