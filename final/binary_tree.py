class BinaryTreeNode:
    def __init__(self, value=None):
        self._value = value
        self._left = None
        self._right = None

    # -------- Value --------
    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

    # -------- Left Child --------
    def set_left(self, node):
        if node is not None and not isinstance(node, BinaryTreeNode):
            raise TypeError("Left child must be a BinaryTreeNode or None")
        self._left = node

    def set_left_value(self, value):
        self._left = BinaryTreeNode(value)

    def get_left(self):
        return self._left

    # -------- Right Child --------
    def set_right(self, node):
        if node is not None and not isinstance(node, BinaryTreeNode):
            raise TypeError("Right child must be a BinaryTreeNode or None")
        self._right = node

    def set_right_value(self, value):
        self._right = BinaryTreeNode(value)

    def get_right(self):
        return self._right

    def print_tree(self, prefix="", is_left=True):
        if self._right is not None:
            self._right.print_tree(prefix + ("│   " if is_left else "    "), False)

        print(prefix + ("└── " if is_left else "┌── ") + str(self._value))

        if self._left is not None:
            self._left.print_tree(prefix + ("    " if is_left else "│   "), True)

