# Definition for singly-linked list.
from typing import Optional , List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = None
        if len(lists) == 1:
            return lists[0]

        if len(lists):
            lst = lists[0]
        else:
            return head
        for x in range(1,len(lists)):
            head = ListNode()
            start = head
            previous = None 
            second_list = lists[x]
            if not lst and not second_list:
                lst = None
                head = None 
                continue

            while True:
                if not lst:
                    if previous:
                        previous.next = second_list
                    else:
                        head = second_list
                    
                    break
                if not second_list:
                    if previous:
                        previous.next = lst
                    else:
                        head = lst

                    break

                if lst.val < second_list.val:
                    start.val = lst.val
                    lst = lst.next
                else:
                    start.val = second_list.val
                    second_list = second_list.next

                a = ListNode()
                start.next = a
                previous = start
                start = a
            
            lst = head
        return head