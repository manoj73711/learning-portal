class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

#Find the middle of linked list
class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def detectLoop(self, head):
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
    def removeLoop(self, head):

        #Step 1: Detect the loop
        fast = head
        slow = head
        loopFound = False
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        #Return the head if no loop is found
        if slow !=fast:
            return head
        slow = head
        while slow.next!=fast.next:
            slow = slow.next
            fast = fast.next
        fast.next = None
        return head

    def detectLengthOfLoop(self, head):

        # Step 1: Detect the loop
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break

        if slow!=fast:
            return 0
        i = 0
        while fast.next!=slow:
            fast = fast.next
            i +=1
        return i+1





