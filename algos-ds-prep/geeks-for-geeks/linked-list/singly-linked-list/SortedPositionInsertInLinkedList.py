class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

#This is a naked eye verified code but not tested
class SinglyLinkedList:

    def __init__(self):
        self.head = None

    #To Insert element in a linkedlist such that list sort is not changed
    def insertAtSortedPosition(self, val):

        temp = Node(val)
        if self.head is None:
            self.head = temp
            return self.head
        if val < self.head.val:
            temp.next = self.head
            self.head = temp
            return self.head

        curr = self.head
        while curr.next is not None and curr.next.val < temp.val:
            curr = curr.next
        temp.next = curr.next
        curr.next = temp
        return self.head
