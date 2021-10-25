class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class SinglyLinkedList:

    def __init__(self):
        self.head = None

    # This segrates all the even and odd values together
    # having same relative order among the nodes in even or odd
    def divide(self, N, head):

        os, oe, es, ee = None, None, None, None
        curr = head
        while curr:
            if curr.data % 2 == 0:
                if es is None:
                    es, ee = curr, curr
                else:
                    ee.next = curr
                    ee = ee.next
            else:
                if os is None:
                    os, oe = curr, curr
                else:
                    oe.next = curr
                    oe = oe.next
            curr = curr.next
        if os or es:
            return
        ee.next = os
        oe.next = None
        head = es
        return head
        # code here
