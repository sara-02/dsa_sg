class N(object):
    def __init__(self, data, link=None):
        self.data = data
        self.link = link


class LL(object):
    def __init__(self):
        self.head = None
    
    def traverse(self):
        temp = self.head
        while temp is not None:
            if temp.link is None:
                print temp.data
            else:    
                print str(temp.data) + "-->",
            temp = temp.link
    
    def insert_first(self, node):
        node.link = self.head
        self.head = node
        return node.link
    
    def insert_last(self, node):
        temp = self.head
        if temp is None:
            return self.insert_first(node)
        while temp.link is not None:
            temp = temp.link
        temp.link = node
        return temp.link
    
    def insert_after(self, node, inode):
            temp = self.head
            while temp != node and temp.link is not None:
                temp = temp.link
            if temp.link is None:
                return None, None
            inode.link = node.link
            node.link = inode
            return node.link, inode.link
    
    def insert_after_pos(self, pos, inode):
        if pos <= 1:
            return self.insert_first(inode)
        temp = self.head
        count = 2
        while count < pos and temp.link is not None:
            temp = temp.link
            count = count + 1

        if temp.link is None:
            temp.link = inode
            inode.link = None
            return inode.link
        inode.link = temp.link
        temp.link = inode
        return inode.link
     
    def delete_head(self):
        if self.head is None:
            return
        temp = self.head
        if temp.link is None:
            self.head = None
            del(temp)
            return
        self.head = self.head.link
        del temp
        
    def delete_last(self):
        if self.head is None:
            return
        temp = self.head
        if temp.link is None:
            self.head = None
            del(temp)
            return
        while temp.link.link is not None:
            temp = temp.link
        temp2 = temp.link
        temp.link = None
        del temp2
    
    def delete_node(self, node):
        if self.head is None:
            return
        temp = self.head
        if temp.link is None:
            self.head = None
            del(temp)
            return
        while temp.link != node and temp.link is not None:
            temp = temp.link
        if temp.link is None:
            return
        elif temp.link.link is None:
            temp2 = temp.link
            temp.link = None
            del temp2
            return
        temp2= temp.link
        temp.link = temp2.link
        temp2.link = None
        del temp2
        return
    
    def delete_pos(self, pos):
        if pos <= 1:
            self.delete_head()
            return
        count = 2
        temp = self.head
        if temp.link is None:
            self.head = None
            del(temp)
            return
        while count < pos and temp.link is not None:
            temp = temp.link
            count = count + 1
        if temp.link is None:
            return
        elif temp.link.link is None:
            temp2 = temp.link
            temp.link = None
            del temp2
            return
        temp2= temp.link
        temp.link = temp2.link
        temp2.link = None
        del temp2
        return     

def main():
	ll = LL()
	n1 = N(5)
	ll.head = n1
	n2 = N(6)
	n3 = N(7)
	n1.link = ll.insert_last(n2)
	n2.link = ll.insert_last(n3)
	ll.traverse()
	n4 = N(4)
	n4.link = ll.insert_first(n4)
	ll.traverse()
	n5 = N(19)
	n2.link, n5.link = ll.insert_after(n2,n5)
	n5.link.data
	ll.traverse()
	n6 = N(-1)
	n6.link = ll.insert_after_pos(-1, n6)
	ll.traverse()
	n7 = N(0)
	n7.link = ll.insert_after_pos(13, n7)
	ll.traverse()
	n8 = N(2)
	n8.link = ll.insert_after_pos(4,n8)
	ll.traverse()
	ll.delete_head()
	ll.traverse()
	ll.delete_last()
	ll.traverse()
	ll.delete_node(n8)
	ll.traverse()
	ll.delete_node(ll.head)
	ll.traverse()
	n20 = N(20)
	ll.delete_node(n20)
	ll.traverse()
	ll.delete_node(n3)
	ll.traverse()
	ll.delete_pos(-1)
	ll.traverse()
	ll.delete_pos(23)
	ll.traverse()
	ll.delete_pos(3)
	ll.traverse()
	ll.delete_pos(3)
	ll.traverse()
	ll2 = LL()
	ll2.insert_last(n20)
	ll2.traverse()
	ll2.delete_last()
	ll2.traverse()

if __name__ == '__main__':
	main()

