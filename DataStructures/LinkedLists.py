import unittest

from Utils.LinkedList import LinkedList
from Utils.Node import Node


def remove_duplicate_nodes(lst):
    head = lst.head
    if head is None or head.next is None:
        return head

    current = head.next

    while current is not None:
        back = head
        while back != current and back:
            if back.data == current.data:
                lst.delete_node(back.data)
            back = back.next

        current = current.next



# tests
class MyTest(unittest.TestCase):
    def test1(self):
        lst = LinkedList(1)
        lst.append_to_tail(2)
        lst.append_to_tail(3)
        lst.append_to_tail(3)
        lst.append_to_tail(4)

        required = LinkedList(1)
        required.append_to_tail(2)
        required.append_to_tail(3)
        required.append_to_tail(4)

        remove_duplicate_nodes(lst)

        lst.to_string()
        self.assertEqual(lst, required)
