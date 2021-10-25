# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':

        if head is None:
            return None
        hmap = {}
        curr = head

        while curr:
            hmap[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            newCurr = hmap[curr]
            if curr.next:
                newCurr.next = hmap[curr.next]
            if curr.random:
                newCurr.random = hmap[curr.random]
            curr = curr.next
        copy = hmap[head]
        return copy
