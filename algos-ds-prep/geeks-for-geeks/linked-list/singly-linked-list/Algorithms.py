class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
#Find the middle of linked list
class SinglyLinkedList:

    def __init__(self):
        self.head = None

    #Remove duplicates from the sorted linked list in efficient manner
    def removeDuplicatesFromSortedLinkedList(self):

        if self.head is None or self.head.next is None:
            return self.head
        curr = self.head
        while curr and curr.next:
            if curr.data == curr.next.data:
                curr.next = curr.next.next
            else:
                curr = curr.next
    #Method 1: reverse the linked list recrusive manner
    def reverseLinkedListRec(self, head):

        if head is None or head.next is None:
            return self.head
        rest_head = self.reverseLinkedListRec(head.next)
        rest_tail = head.next
        rest_tail.next = head
        head.next = None
        return rest_head
    # Method 2: reverse the linked list in groups k
    def reverseInGroups(self, k):

        if self.head is None or self.head.next is None:
            return self.head

        prev, next = None, None
        curr = self.head

        count = 0
        while curr and count < k:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            count +=1



    # Method 2: reverse the linked list
    def reverseLinkedListIterative(self):

        prev = None
        curr = self.head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

    #Find the nth node from the end
    def findNthNodeFromEnd(self, n):

        if self.head is None:
            return self.head
        first = self.head
        #Move first pointer n nodes first
        for i in range(n):
            if first is None:
                return None
            first = first.next
        second = self.head
        #Move the second and first pointer in same speed until first becomes null
        while first:
            first = first.next
            second = second.next
        return second.data

    #This is more efficient solution ref: gfg
    def findMiddle(self):

        if self.head is None:
            return self.head
        slow, fast = self.head, self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

        # Below ugly is my initial solution that i cameup with
        # if self.head is None or self.head.next is None:
        #     return self.head.val
        # elif self.head.next.next is None:
        #     return self.head.next.val
        #
        # first = self.head
        # second = self.head.next.next
        #
        # while second is not None:
        #     first = first.next
        #     second = second.next.next
        # return first
