# Function to convert a binary tree to doubly linked list.
class Solution:

    def __init__(self):
        self.head = None
        self.tail = None

    def bToDLL(self, root):

        if not root:
            return
        self.bToDLL(root.left)
        node = root
        if self.head is None:
            self.head = node
        else:
            self.tail.right = node
            node.left = self.tail
        self.tail = node

        self.bToDLL(root.right)

        return self.head

        # do Code here
