from Utils.Node import Node


class LinkedList:

    def __init__(self, data):
        self.head = Node(data)

    # append data as node in the end of a linked list
    def append_to_tail(self, data):
        end = Node(data)
        n = self.head

        while n.next is not None:
            n = n.next

        n.next = end

    # delete node from linked list with given data
    def delete_node(self, data):
        prev = None
        curr = self.head
        while curr:
            if curr.data == data:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next

            prev = curr
            curr = curr.next



    def to_string(self):
        n = self.head
        while n is not None:
            print n.data,
            if n.next is not None:
                print " -->",

            n = n.next

    def __eq__(self, other):
        current = self.head
        other = other.head

        if other is None:
            return False

        while current:

            if other.data != current.data:
                return False

            current = current.next
            other = other.next

        if other:
            return False

        return True

    def __ne__(self, other):
        return not self == other

