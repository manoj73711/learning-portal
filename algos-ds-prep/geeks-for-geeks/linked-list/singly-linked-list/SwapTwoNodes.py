class ListNode:
    def __init__(self, val):
        self.data = val
        self.next = None

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        dummy = ListNode(-1)
        dummy.next = curr

        prev_node = dummy

        while curr and curr.next:
            # Nodes to be swapped
            first = curr
            second = curr.next

            # Swapping
            prev_node.next = second
            first.next = second.next
            second.next = first

            # Reinitializing the head and prev_node for next swap
            prev_node = first
            curr = first.next

        return dummy.next

