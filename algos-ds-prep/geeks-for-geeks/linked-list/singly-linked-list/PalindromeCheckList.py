# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        if head is None:
            return True
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        rev = self.reverseLinkedList(slow.next)
        curr = head

        while rev:
            if rev.val != curr.val:
                return False
            rev = rev.next
            curr = curr.next
        return True

    def reverseLinkedList(self, head):
        if head is None or head.next is None:
            return head
        rest_head = self.reverseLinkedList(head.next)
        rest_tail = head.next
        rest_tail.next = head
        head.next = None
        return rest_head
