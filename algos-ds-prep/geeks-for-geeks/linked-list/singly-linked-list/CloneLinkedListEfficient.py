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
        curr = head
        while curr:
            originalNext = curr.next
            curr.next = Node(curr.val)
            curr.next.next = originalNext
            curr = originalNext

        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            else:
                curr.next.random = None
            curr = curr.next.next

        original = head
        copy = head.next
        temp = copy
        while original and copy:
            self.groupOriginal(original)
            self.groupOriginal(copy)
            original = original.next
            copy = copy.next

        return temp

    def groupOriginal(self, node):

        if node.next:
            node.next = node.next.next
        else:
            node.next = node.next


