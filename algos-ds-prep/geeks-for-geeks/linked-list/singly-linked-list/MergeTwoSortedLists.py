#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#This code is tested in leetcode
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        if l1 is None:
            return l2
        if l2 is None:
            return l1

        head, tail = None, None

        if l1.val < l2.val:
            head = tail = l1
            l1 = l1.next
        else:
            head = tail = l2
            l2 = l2.next

        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                tail = l1
                l1 = l1.next
            else:
                tail.next = l2
                tail = l2
                l2 = l2.next
        if l1 is None:
            tail.next = l2
        else:
            tail.next = l1

        return head
