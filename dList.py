class dList:

        head = None
        tail = None

        class Node:
            value = None
            nextNode = None
            prevNode = None

            def __init__(self, value, nextNode=None,prevNode=None):
                self.value = value
                self.nextNode = nextNode
                self.prevNode = prevNode

        def push_front(self, value):
            node = self.Node(value)
            if self.head == None:
                self.head = node
                self.tail = node
            else:
                node.nextNode = self.head
                self.head.prevNode = node
                self.head = node

        def print(self):
            if self.head == None:
                print("list is empty")
            else:
                node = self.head
                while node.nextNode:
                    print(f"{node.value}", end=", ")
                    node = node.nextNode
                print(node.value)

        def pop_front(self):
            if self.head:
                if  self.head.nextNode == None:
                    self.head = None
                    self.tail = None
                else:
                    self.head.prevNode = None
                    self.head = self.head.nextNode


        def push_back(self, value):
            node = self.Node(value)

            if self.head == None:
                self.head = node

            else:
                node.prevNode = self.tail
                self.tail.nextNode = node
            self.tail = node

        def pop_back(self):
            if self.tail == None:
                print("list is empty")
            if self.tail == self.head:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prevNode
                self.tail.nextNode = None


        def contains(self, value):
            if self.head == None:
                print("list is empty")
            else:
                flag = False
                node = self.head
                while node:
                    if node.value == value:
                        flag = True

                    node = node.nextNode

                return flag

        def sort(self):
            if self.head and self.head.nextNode:
                flag = True
                while flag:
                    flag = False
                    node = self.head
                    while node:
                        if node.nextNode:
                            if node.value > node.nextNode.value:
                                flag = True
                                before = node.prevNode
                                cur = node
                                next = node.nextNode
                                after = next.nextNode
                                cur.prevNode = next
                                cur.nextNode = after
                                next.prevNode = before
                                next.nextNode = cur
                                if before:
                                    before.nextNode = next
                                else:
                                    self.head = next
                                if after:
                                    after.prevNode = cur
                                else:
                                    self.tail = cur
                        node = node.nextNode

        def revers(self):
            if self.head:
                if self.head.nextNode:
                    cur = self.head
                    while cur:
                        temp = cur.nextNode
                        cur.nextNode = cur.prevNode
                        cur.prevNode = temp
                        cur = temp
                    self.head = self.tail
                else:
                    return  self.head




my_list = dList()
for i in range(1,6):
    my_list.push_front(i)
my_list.print()
my_list.revers()
my_list.print()




