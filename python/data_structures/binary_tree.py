class BinaryTree:
    """
    Put docstring here
    """

    def __init__(self, root=None):
        self.root = root

    # root left right
    def pre_order(self):
        traversal = []

        def walk(root):
            if root:
                # root
                traversal.append(root.value)  # operation
                # left
                walk(root.left)
                # right
                walk(root.right)

        # remember to invoke it
        walk(self.root)

        return traversal


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
