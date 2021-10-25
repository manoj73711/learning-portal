class Node:

    def __init__(self, val):
        self.data = val
        self.next = None

class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def reverseLinkedListInGroupsIterativeForm(self, head):
        curr = head
        prev, next = None
        count = 0
        while curr and count < k:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            count +=1
        if next:
            rest_head = self.reverseLinkedListInGroupsIterativeForm(next, k)
            head.next = rest_head
        return prev

    def reverseLinkedListInGroupsIterativeForm(self, head):

        prevFirst = None
        curr = head
        isFirstPass = True
        while curr:
            first = curr, prev = None
            count = 0
            while curr and count< k:
                next = curr.next85
                curr.next =prev
                prev = curr
                curr = next
                count +=1
            if isFirstPass:
                head = prev
                isFirstPass = True
            else:
                prevFirst.next = prev
            prevFirst = first

        return head