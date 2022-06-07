from binarytree import BinaryTree


def main():
    tree = BinaryTree(5, 5)
    tree.insert(7, 6)
    tree.insert(2, 3)
    tree.insert(4, 7)
    tree.insert(-2, 5)
    tree.insert(-5, -4)
    tree.insert(6, 3)
    tree.insert(-7, -14)
    tree.insert(-3, -2)
    tree.insert(-5, -4)
    tree.insert(9, 3)
    tree.insert(6, 8)
    tree.insert(5, 2)
    tree.print_positive_y(tree)
    tree.print_all_nodes(tree)


if __name__ == '__main__':
    main()
