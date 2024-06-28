from stack_linked_list import Stack


def display(head):
    num = 1
    while head:
        print("element: %s"%num,head.val)
        head = head.next
        num += 1

def swapping_of_adjecent_node(head,index):
    start = head
    num = 1
    if index == 1:
        a = start
        b = a.next
        if b.next:
            c = b.next
        else:
            return head
        d = c.next
        b.next = a
        a.next = c
        return b
    while start:
        if num == index-1:
            a = start
            b = a.next
            if b.next:
                c = b.next
            else:
                break
            d = c.next
            a.next = c
            c.next = b
            b.next = d
            break
        start = start.next
        num += 1

    return head

if __name__ == "__main__":
    s = Stack()
    s.add(1)
    s.add(11)
    s.add(111)
    s.add(1111)
    s.add(1111)
    s.add(1123)
    s.add(1321)
    s.add(1153)
    s.display()
    a = swapping_of_adjecent_node(s.head,1)
    display(a)
    a = swapping_of_adjecent_node(s.head,5)
    display(a)


