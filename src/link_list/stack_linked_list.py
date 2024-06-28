from link_node import LinkNode
from typing import List

'''
stack follow LIFO which means the elements are added in head and removed from head.
stack implementaion
12 -> Head
12 -> 13 -> Head
12 -> 13 -> 14 -> Head

Head is shifting as the element are added.

'''


class Stack():
    head = None
    len = 0

    # Insertion
    def add(self, val:int):
        self.head = LinkNode(val = val , next = self.head)
        self.len += 1
        return 1
    # deletion
    def pop(self) -> int:
        if self.head:

            val = self.head.val
            self.head = self.head.next
            self.len -=1
            return val
        return -1
    # searching
    def search(self,val:int) -> str:
        start = self.head
        while start:
            if start.val == val:
                return "Item in the linked list"
            start = start.next
        return "Item Not Found"

    # Iteration 
    def display(self):
        start = self.head
        while start:
            print(start.val)
            start = start.next

    def reverse(self):
        start = self.head
        tail = None

        while start:
            next_element = start.next
            start.next = tail
            tail = start
            start = next_element
        
        self.head = tail
    
    def length(self):
        start = self.head
        len = 0
        while start:
            start = start.next
            len += 1
        
        return len


if __name__ == "__main__":
    s = Stack()
    # Insertion and Traversing
    s.display()
    s.add(12)
    s.add(112)
    s.add(121)
    print(s.len)
    s.add(120)
    s.add(125)
    s.add(122)
    print(s.len)
    s.display()

    # Search
    print(s.search(120))
    print(s.search(112))
    print(s.search(102))
    
    # deletion
    s.display()
    print("deleted Value: ",s.pop())
    print("deleted Value: ",s.pop())
    s.display()

    r = Stack()
    print(r.pop())
    print(r.len)
    print(r.length())
    print(r.display())
    print(r.search(23))

    s.display()
    s.reverse()
    s.display()
    print(s.length())

