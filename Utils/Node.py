
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


    # append data as node in the end of a linked list
    def append_to_tail(self, data):
        end = Node(data)
        n = self

        while n.next is not None:
            n = n.next

        n.next = end

    # delete node from linked list with given data
    def delete_node(self, data):
        if self.data == data:
            return self.next

        n = self

        while n.next is not None:
            if n.next.data == data:
                n.next = n.next.next

            n = n.next

    def to_string(self):
        n = self
        while n is not None:
            print n.data,
            if n.next is not None:
                print " -->",

            n = n.next