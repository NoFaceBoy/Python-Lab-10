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

    def remove_negative_x_y(self, root) -> None:
        if root is not None:
            self.remove_negative_x_y(root.left)
            if root.y < 0 and root.x < 0:
                self.delete_node(self, root.y)
            self.remove_negative_x_y(root.right)

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

    def delete_node(self, root, key):
        if root is None:
            return root
        if key == root.y:
            if root.left is None:
                root = root.right
            elif root.right is None:
                root = root.left
            else:
                while root.left is not None:
                    root = root.left
                root.right = self.delete_node(root.right, key)
        elif key < root.y:
            root.left = self.delete_node(root.left, key)
        else:
            root.right = self.delete_node(root.right, key)
        return root
