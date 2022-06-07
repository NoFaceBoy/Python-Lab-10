class BinaryTree:
    def __init__(self, x, y):
        self.left = None
        self.right = None
        self.x = x
        self.y = y

    def insert(self, x, y):
        if y < self.y:
            if self.left is None:
                self.left = BinaryTree(x, y)
            else:
                self.left.insert(x, y)
        elif y > self.y:
            if self.right is None:
                self.right = BinaryTree(x, y)
            else:
                self.right.insert(x, y)

    def remove_negative_x_y(self) -> None:
        pass

    def print_positive_y(self, root) -> None:
        if root is not None:
            self.print_positive_y(root.left)
            if root.y > 0:
                print("(" + str(root.x) + "; " + str(root.y) + ")")
            self.print_positive_y(root.right)

    def print_all_nodes(self, root):
        if root is not None:
            print("(" + str(root.x) + "; " + str(root.y) + ")")
            self.print_all_nodes(root.left)
            self.print_all_nodes(root.right)
