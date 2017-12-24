"""Create a mirror/inversion of a given binary tree."""
# Reference link: https://www.geeksforgeeks.org/write-an-efficient-c-function-to-convert-a-tree-into-its-mirror-tree/


class Node(object):
    """Class to create Node object."""

    def __init__(self, data=None, left=None, right=None):
        """Initialise a node with data, and left-right child pointers."""
        self.data = data
        self.left = left
        self.right = right


class BinaryTree(object):
    """Class to form a binary tree and perform actions on it."""

    def __init__(self, root=None):
        """Initialise a binary tree with root pointer."""
        self.root = root

    def inorder(self, root):
        """Print the inorder traversal."""
        if root:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)

    def mirror(self, root):
        """Generate the mirror starting from root of the tree."""
        if root:
            self.mirror(root.left)
            self.mirror(root.right)
            root.left, root.right = root.right, root.left


def main():
    # Generate nodes for the tree
    node_list = []
    for i in range(1, 8):
        node_list.append(Node(i))
    # Attach child nodes to parent
    node_list[0].left = node_list[1]
    node_list[0].right = node_list[2]
    node_list[1].left = node_list[3]
    node_list[3].left = node_list[5]
    node_list[3].right = node_list[6]
    node_list[2].right = node_list[4]
    # Form the Binary tree
    bt = BinaryTree(root=node_list[0])
    assert bt.root.data == 1
    # Assign a temp_root for traversal
    print("Inorder of the Tree Before inversion:")
    # Expected Order: 6,4,7,2,1,3,5
    temp_root = bt.root
    bt.inorder(temp_root)
    # Invert the tree
    bt.mirror(bt.root)
    print("Inorder of the Tree After inversion:")
    # Expected Order: 5,3,1,2,7,4,6
    root = bt.root
    bt.inorder(root)
    # Time complexity: O(n)


if __name__ == '__main__':
    main()
