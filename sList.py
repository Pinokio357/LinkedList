class sList:
    head = None

    class Node:
        value = None
        nextNode = None

        def __init__(self, value, nextNode = None):
            self.value = value
            self.nextNode = nextNode


    def push_front(self, value):
        node = self.Node(value)
        if self.head == None:
            self.head = node
        else:
            node.nextNode = self.head
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
        if self.head == None:
            print ("list is empty")
        else:
            self.head = self.head.nextNode

    def push_back(self, value):
        node = self.Node(value)
        curr = self.head
        if self.head == None:
            self.head = node
        else:
            while curr.nextNode:
                curr = curr.nextNode
            curr.nextNode = node

    def pop_back(self):
        curr = self.head
        if self.head == None:
            print ("list is empty")
        else:
            if self.head.nextNode == None:
                self.head = None
            else:
                while curr.nextNode.nextNode != None:
                    curr = curr.nextNode
                curr.nextNode = None

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
    def revers(self):
        if self.head:
            if self.head.nextNode:
                prev = None
                cur = self.head
                while cur:
                    next = cur.nextNode
                    cur.nextNode = prev
                    prev = cur
                    cur = next
                self.head = prev





my_list = sList()
for i in range(1, 6):
  my_list.push_front(i)

my_list.print()

my_list.revers()
my_list.print()


