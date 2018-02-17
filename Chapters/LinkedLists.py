import unittest

from DataStructures.LinkedList import LinkedList


# Question 1
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


# Question 2
def find_nth(lst, n):
    last = lst.head
    for i in range(n):
        if not last:
            return None
        last = last.next

    ans = lst.head

    while last:
        last = last.next
        ans = ans.next

    return ans.data


# Question 3
def remove_node_from_middle(n):
    if n.next:
        n.data = n.next.data
        n.next = n.next.next

    else:
        # Problem to delete last node
        None


# Question 4
def add_lists(lst1, lst2):
    h1 = lst1.head
    h2 = lst2.head

    ans = LinkedList()

    carry = 0

    while h1 or h2:
        if not h1:
            result = h2.data + carry
            h1 = h1.next

        elif not h2:
            result = h1.data + carry
            h2 = h2.next

        else:
            result = h1.data + h2.data + carry
            h1 = h1.next
            h2 = h2.next

        carry = 1 if result >= 10 else 0

        ans.append_to_tail(result - carry * 10)

    return ans

def is_circular(lst):
    if lst.head is None:
        return False

    if lst.head.next is None:
        return False

    slow = lst.head
    fast = lst.head.next

    while True:
        if slow == fast:
            return True

        slow = slow.next
        if fast.next and fast.next.next:
            fast = fast.next.next
        else:
            return False

# tests
class LinkedListTest(unittest.TestCase):
    def test1(self):
        lst = LinkedList(1, 2, 3, 3, 4)

        required = LinkedList(1, 2, 3, 4)

        remove_duplicate_nodes(lst)

        self.assertEqual(lst, required)

    def test2(self):
        lst = LinkedList(1, 1, 3, 1, 1)

        self.assertEqual(find_nth(lst, 3), 3)

    def test3(self):
        lst = LinkedList(1, 1, 3, 1, 1)

        n = lst.get_node(3)

        remove_node_from_middle(n)

        required = LinkedList(1, 1, 1, 1)

        self.assertEqual(lst, required)

    def test4(self):
        lst1 = LinkedList(3, 1, 5)
        lst2 = LinkedList(5, 9, 2)

        required = LinkedList(8, 0, 8)

        ans = add_lists(lst1, lst2)

        self.assertEqual(ans, required)


    def test5(self):
        lst = LinkedList(1,2,3,4,5)

        n = lst.get_node(3)

        lst.get_node(5).next = n

        self.assertEqual(is_circular(lst), True)

        lst1 = LinkedList(1,2,3,4)

        self.assertEqual(is_circular(lst1), False)
