from DataStructures.TreeNode import TreeNode


class BSTree:
    def __init__(self, root=None):
        self.root = TreeNode(root)

    def insert(self, value, current_node=None):
        if not current_node:
            current_node = self.root

        if current_node.data == value:
            return

        if current_node.data > value:
            if current_node.left:
                self.insert(value, current_node.left)
            else:
                current_node.left = TreeNode(value, current_node)
        else:
            if current_node.right:
                self.insert(value, current_node.right)
            else:
                current_node.right = TreeNode(value, current_node)

