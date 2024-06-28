from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        head = ListNode() 
        start = head
        previous = None
        while list1 or list2:
            if not list1 :
                if previous:
                    previous.next = list2
                else:
                    head = list2
                break
            if not list2:
                if previous:
                    previous.next = list1
                else:
                    head = list1
                break
            if list1.val < list2.val :
                start.val = list1.val
                a = ListNode()
                start.next = a
                previous = start
                start = a
                list1 = list1.next
            else:
                start.val = list2.val
                a = ListNode()
                start.next = a
                previous = start
                start = a
                list2 = list2.next
        return head

        