class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
    # add code here

class CircularLinkedList:

    def __init__(self):
        self.head = None

    # Function to insert node at the beginning of the circular linked list
    def pushAtBeginning(self, data):

        new_node = Node(data)

        if self.head is None:
            new_node.next = new_node
            return new_node

        new_node.next = self.head.next
        self.head.next = new_node

        # Swap data for head and next
        self.head.data, new_node.data = new_node.data, self.head.data

        return self.head

    # This is to delete the head of circular linked list
    def deleteHead(self):

        if self.head is None or self.head.next is self.head:
            return None

        self.head.data = self.head.next.data
        self.head.next = self.head.next.next

        return self.head

    # This is to push at ending
    def pushAtEnding(self, data):

        new_node = Node(data)

        if self.head is None:
            new_node.next = new_node
            return new_node

        new_node.next = self.head.next
        self.head.next = new_node

        # Swap data for head and next
        self.head.data, new_node.data = new_node.data, self.head.data

        return new_node

    # This is to push at ending
    def deleteKth(self, k):

        if self.head is None:
            return self.head

        if k == 1:
            return self.deleteHead()

        curr = self.head

        for i in range(0, k - 2):
            curr = curr.next
        curr.next = curr.next.next
        return self.head

    #  Function to print nodes in a given Circular linked list
    def printList(self):

        if self.head is None:
            return
        print(self.head.data)
        temp = self.head.next
        while temp != self.head:
            print(temp.data)
            temp = temp.next
