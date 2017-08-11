# coding: utf-8


class N():

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class T():

    def __init__(self):
        self.root = None

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data)

    def height(self, root):
        if root is None:
            return 0
        else:
            lh = self.height(root.left)
            rh = self.height(root.right)
            if lh >= rh:
                return lh + 1
            else:
                return rh + 1

    def levelorder(self, root):
        h = self.height(root)
        for l in range(1, h + 1):
            self.level_data_print(root, l)

    def level_data_print(self, root, level):
        if root is None:
            return
        if level == 1:
            print root.data
        else:
            self.level_data_print(root.left, level - 1)
            self.level_data_print(root.right, level - 1)


def main():
    n1 = N(1)
    n2 = N(2)
    n3 = N(3)
    n4 = N(4)
    n5 = N(5)
    n6 = N(6)
    n1.right = n2
    n2.right = n5
    n5.right = n6
    n5.left = n3
    n3.right = n4
    t = T()
    t.root = n1
    print "\n######### INORDER"
    root = t.root
    t.inorder(root)
    print "\n######### PREORDER"
    root = t.root
    t.preorder(root)
    print "\n######### POSTORDER"
    root = t.root
    t.postorder(root)
    print "\n######### LEVELORDER"
    root = t.root
    t.levelorder(root)
    print "\n######### HEIGHT"
    root = t.root
    print(t.height(root))

if __name__ == '__main__':
    main()
