class Tree:
    def __init__(self, data):
        self.left = None
        self.data =data
        self.right = None

class Solution:

    #Binary search tree search operation
    #TC: o(h) , sc o(h)

    def search(self, root, key):

        if root is None:
            return False
        elif root.data == key:
            return True
        elif root.data < key:
            return self.search(root.right, key)
        else:
            return self.search(root.left, key)

    # TC: o(h) , sc o(h)
    def insert(self, root, key):

        if root is None:
            return Tree(root.value)
        elif root.data < key:
            root.right = self.insert(root.right, key)
        elif root.data > key:
            root.left = self.insert(root.left, key)
        return root

    #TC: o(n), SC: o(1)
    def insert_iterative(self, root, key):

        temp = Tree(key)
        curr = root
        parent = None

        while curr:
            parent = curr

            if curr.data < key:
                curr = curr.right
            elif curr.data > key:
                curr = curr.right
            else:
                return root
        if parent is None:
            return temp
        if parent.key < key:
            parent.right = temp
        if parent.key > key:
            parent.left = temp
        return root

        if root is None:
            return Tree(root.value)
        elif root.data < key:
            root.right = self.insert(root.right, key)
        elif root.data > key:
            root.left = self.insert(root.left, key)
        return root

    #This is to delete the node
    #Working code in leetcode
    #TC: o(h), SC: o(h)
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root:
            return None

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                node = self.findSuccessor(root)
                root.val = node.val
                root.right = self.deleteNode(root.right, node.val)
        return root

    def findSuccessor(self, node):
        curr = node.right
        while curr and curr.left:
            curr = curr.left
        return curr
        # code here.



