class Node:
    def _init_(self, val):
        self.data = val
        self.left = None
        self.right = None

    # Function to return a list containing elements of left view of the binary tree.
    def LeftView1(self, root):
        maxlevel = [0] * 1
        self.LeftViewRec(root, 1, maxlevel)

    def LeftViewRec(self, root, level: int, maxlevel: [int]):
        if root is None:
            return
        if maxlevel[0] < level:
            print(root.data)
            maxlevel[0] = level
        self.LeftViewRec(root.left, level + 1, maxlevel)
        self.LeftViewRec(root.right, level + 1, maxlevel)

    #Solution:2 iterative
    def leftViewUtil(self, root):

        if root is None:
            return False
        que = []
        que.append(root)
        while len(que) > 0:
            size = len(que)
            for i in range(size):
                node = que.pop()
                if i == 0:
                    print (node.data)
                left = 0
                right = 0
                if node.left is not None:
                    left = node.left.data
                    que.append(node.left)
                if node.right is not None:
                    right = node.right.data
                    que.append(node.right)
                if node.data !=left+right:
                    return False
        return False