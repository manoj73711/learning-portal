class Node:

    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:

    def __init__(self):
        self.head =None

    def insertAtHead(self, val):
        #Case to handle when head is empty
        node = Node(val)

        if self.head is None:
            node.next = node
            node.prev = node
            self.head = node
            return self.head

        #When head is not none

        node.prev = self.head.prev
        node.next = self.head
        self.head.prev.next = node
        self.head.prev = node
        self.head = node

        return self.head
