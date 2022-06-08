from binarytree import BinaryTree


def main():
    tree = BinaryTree(5, 5)
    tree.insert(7, 6)
    tree.insert(2, 3)
    tree.insert(-4, 7)
    tree.insert(-2, 15)
    tree.insert(-5, -4)
    tree.insert(6, 12)
    tree.insert(-7, -14)
    tree.insert(-3, -2)
    tree.insert(-5, -7)
    tree.insert(9, 16)
    tree.insert(-6, 8)
    tree.insert(5, 2)
    print("All nodes top down traversal")
    tree.print_all_nodes(tree)
    print("Only positive y")
    tree.print_positive_y(tree)
    print("All nodes are still there")
    tree.print_all_nodes(tree)
    print("Deleting with negative x and y")
    tree.remove_negative_x_y(tree)
    print("Printing nodes that are left")
    tree.print_all_nodes(tree)


if __name__ == '__main__':
    main()
