from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        start = head
        while start:
            size += 1
            start = start.next
        if n == size:
            head = head.next
        index = size - n 
        num = 1
        start = head
        while start:
            if num == index:
                if n == 1:
                    start.next = None
                    break
                else:
                    start.next = start.next.next
                    break
            start = start.next
            num += 1
        return head


        
        