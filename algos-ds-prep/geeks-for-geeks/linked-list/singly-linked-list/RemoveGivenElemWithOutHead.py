class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


# Given an element and delete its node from the linked list where head is unknown
class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def removeElement(self, node):
        if node is None or node.next is None:
            return None
        node.data = node.next.data
        node.next = node.next.next
        return node
