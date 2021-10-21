
#This is solution 1
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        return self.isValidBSTHelper(root, float('-inf'), float('inf'))

    def isValidBSTHelper(self, root, minVal, maxValue):

        if not root:
            return True

        return minVal < root.val and root.val < maxValue and self.isValidBSTHelper(root.left, minVal, root.val) and self.isValidBSTHelper(root.right, root.val, maxValue)

#This is also efficient solution with one pass
class Solution:

    def isValidBST(self, root) -> bool:
        prevValue = [float('-inf')]
        return self.isValidBSTHelper(root, prevValue)

    def isValidBSTHelper(self, root, prevValue) -> bool:

        if root is None:
            return True

        if self.isValidBSTHelper(root.left, prevValue) is False:
            return False

        if root.val <= prevValue[0]:
            return False
        prevValue[0] = root.val

        return self.isValidBSTHelper(root.right, prevValue)

