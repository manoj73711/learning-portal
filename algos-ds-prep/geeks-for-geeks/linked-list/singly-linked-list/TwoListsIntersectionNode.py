# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#This solution is test in lc
class Solution:

    def getCount(self, node):
        c = 0
        while node:
            node = node.next
            c += 1
        return c

    def _getIntersectionNode(self, d, head1, head2):
        p1 = head1
        p2 = head2

        for i in range(d):
            if p1 is None:
                return None
            p1 = p1.next

        while p1 and p2:

            if p1 is p2:
                return p1

            p1 = p1.next
            p2 = p2.next
        return None

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None

        # Traverse the head 1 for c1
        # travese the head 2 for c2
        # Find the d = diff of c1 and c2
        # start pointers for both lists from head p1 and p2
        # Find the bigger one among p1 and p2
        # move the bigger one for d distance
        # Now move the pointers at same speed with one step
        # Look for p1 and p2 where they becomes equal
        # return that node

        c1, c2 = self.getCount(headA), self.getCount(headB)

        d = abs(c1 - c2)

        if c1 > c2:
            return self._getIntersectionNode(d, headA, headB)
        else:
            return self._getIntersectionNode(d, headB, headA)

