# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if self.isBalancedUtil(root, 0) == -1:
            return False
        else:
            return True

    def isBalancedUtil(self, root, height):

        if root is None:
            return height

        lh = self.isBalancedUtil(root.left, height + 1)
        if lh == -1:
            return -1
        rh = self.isBalancedUtil(root.right, height + 1)
        if rh == -1:
            return -1

        if abs(lh - rh) > 1:
            return -1
        return max(lh, rh)
