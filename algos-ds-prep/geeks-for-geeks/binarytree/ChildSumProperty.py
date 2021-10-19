class Solution:

    def isChildSumPropertyRecursion(self, root):

        if root is None:
            
    # Solution:2 iterative
    def isChildSumProperty(self, root):

        if root is None:
            return False
        que = []
        que.append(root)
        while len(que) > 0:
            size = len(que)
            for i in range(size):
                node = que.pop()
                if i == 0:
                    print(node.data)
                left = 0
                right = 0
                if node.left is not None:
                    left = node.left.data
                    que.append(node.left)
                if node.right is not None:
                    right = node.right.data
                    que.append(node.right)
                if node.data != left + right:
                    return False
        return False