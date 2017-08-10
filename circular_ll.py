# circular linked list


class N(object):

    def __init__(self, data, link=None):
        self.data = data
        self.link = link


class LL(object):

    def __init__(self):
        self.head = None

    def traverse(self):
        temp = self.head
        if temp is None:
            return
        print temp.data,
        while temp.link != self.head:
            temp = temp.link
            print "--> " + str(temp.data),
        print "\n"

    def count_len(self):
        temp = self.head
        if temp is None:
            return 0
        l = 1
        while temp.link is not self.head:
            temp = temp.link
            l = l + 1
        return l

    def insert_first(self, node):
        temp = self.head
        if temp is None:
            self.head = node
            node.link = node
            return
        while temp.link != self.head:
            temp = temp.link
        node.link = temp.link
        temp.link = node
        self.head = node

    def insert_last(self, node):
        temp = self.head
        if temp is None:
            self.head = node
            node.link = node
            return
        while temp.link != self.head:
            temp = temp.link
        node.link = temp.link
        temp.link = node

    def insert_after(self, node, inode):
        temp = self.head
        while temp != node and temp.link is not self.head:
            temp = temp.link
        inode.link = node.link
        node.link = inode

    def insert_after_pos(self, pos, inode):
        if pos <= 1:
            self.insert_first(inode)
        temp = self.head
        count = 2
        while count < pos and temp.link is not self.head:
            temp = temp.link
            count = count + 1
        inode.link = temp.link
        temp.link = inode

    def delete_head(self):
        if self.head is None:
            return
        temp = self.head
        if temp.link is self.head:
            self.head = None
            del(temp)
            return
        while temp.link != self.head:
            temp = temp.link
        temp2 = self.head
        self.head = self.head.link
        temp.link = self.head
        del(temp2)

    def delete_last(self):
        if self.head is None:
            return
        temp = self.head
        if temp.link is self.head:
            self.head = None
            del(temp)
            return
        while temp.link.link is not self.head:
            temp = temp.link
        temp2 = temp.link
        temp.link = temp2.link
        del(temp2)

    def delete_node(self, node):
        if self.head is None:
            return
        temp = self.head
        if temp.link is self.head:
            self.head = None
            del(temp)
            return
        if node is self.head:
            self.delete_head()
        while temp.link != node and temp.link is not self.head:
            temp = temp.link
        if temp.link is self.head:
            return
        elif temp.link.link is self.head:
            temp2 = temp.link
            temp.link = self.head
            del(temp2)
            return
        temp2 = temp.link
        temp.link = temp2.link
        del(temp2)
        return

    def delete_pos(self, pos):
        if pos <= 1:
            self.delete_head()
            return
        count = 2
        temp = self.head
        if temp.link is self.head:
            self.head = None
            del(temp)
            return
        while count < pos and temp.link is not self.head:
            temp = temp.link
            count = count + 1
        if temp.link is self.head:
            return
        elif temp.link.link is self.head:
            temp2 = temp.link
            temp.link = self.head
            del(temp2)
            return
        temp2 = temp.link
        temp.link = temp2.link
        del temp2
        return


def main():
    n1 = N(1)
    n2 = N(2)
    n3 = N(3)
    n4 = N(4)
    n1.link = n2
    n2.link = n3
    n3.link = n4
    ll = LL()
    ll.head = n1
    n4.link = ll.head
    ll.traverse()
    n5 = N(5)
    ll.insert_first(n5)
    ll.traverse()
    n6 = N(6)
    ll.insert_first(n6)
    ll.traverse()
    n7 = N(7)
    ll.insert_last(n7)
    ll.traverse()
    n8 = N(8)
    ll.insert_after(n3, n8)
    ll.traverse()
    n9 = N(9)
    ll.insert_after(n7, n9)
    ll.traverse()
    n10 = N(10)
    ll.insert_after(n6, n10)
    ll.traverse()
    ll.delete_head()
    ll.traverse()
    ll.delete_last()
    ll.traverse()
    ll.delete_node(n1)
    ll.traverse()
    ll.delete_node(n10)
    ll.traverse()
    ll.delete_node(n7)
    ll.traverse()
    ll.delete_pos(-9)
    ll.traverse()
    ll.delete_pos(19)
    ll.traverse()
    ll.delete_pos(2)
    ll.traverse()
    ll.delete_pos(3)
    ll.traverse()
    print "Len is %d" % ll.count_len()

if __name__ == '__main__':
    main()
