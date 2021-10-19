class Node:
    def _init_(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:

    def maxValueInBinaryTree(self,tree: Node):

        if tree is None:
            return 0
        leftVal = max(tree.data, self.maxValueInBinaryTree(tree.left))
        rightVal = max(tree.data, self.maxValueInBinaryTree(tree.right))

        return max(leftVal, rightVal)