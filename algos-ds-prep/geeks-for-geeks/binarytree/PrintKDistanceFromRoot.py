dclass Node:
    def _init_(self, val):
        self.data = val
        self.left = None
        self.right = None

def printKdistance(root, k):
    if root is None:
        return
    if k == 0:
        print(root.data, end="")
    else:
        printKdistance(root.left, k - 1)
        printKdistance(root.right, k - 1)
