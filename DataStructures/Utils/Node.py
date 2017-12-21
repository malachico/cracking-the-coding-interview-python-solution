
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


        # append data as node in the end of a linked list
        def append_to_tail(data):
            end = Node(data)
            n = self

            while self.next is not None:
                n = self.next

            n.next = end

        # delete node from linked list with given data
        def delete_node(data):
            if self.data == data:
                return self.next

            n = self

            while n.next is not None:
                if n.next.data == data:
                    n.next = n.next.next

                n = n.next