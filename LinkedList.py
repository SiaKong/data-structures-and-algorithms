class Node:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next = next_node
        self.prev = prev_node #for doubly/circular

class LinkedList:
    def __init__(self):
        self.head = None

    def printval(self):
        curr = self.head
        while curr is not None:
            print (curr.value)
            curr = curr.next

    #O(n)
    def insert_last(self, value):
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = value

    #O(1)
    def insert_front(self, value):
        new = value
        new.next = self.head
        self.head = new

    #O(1)
    def remove_front(self):
        if self.head is not None:
            self.head = self.head.next

    #O(N)
    def remove_last(self):
        if self.head is not None:
            curr = self.head
            hold = None
            while curr.next is not None:
                hold = curr
                curr = curr.next
            if hold is None:
                self.head = None
            else:
                hold.next = None

n1 = Node("One")
n2 = Node("Two")
n3 = Node("Three")
n0 = Node("Zero")

n1.next = n2

list = LinkedList()
list.head = n1

list.printval()
print()

list.insert_last(n3)
list.printval()
print()

list.insert_front(n0)
list.printval()
print()

list.remove_front()
list.printval()
print()

list.remove_last()
list.printval()
print()