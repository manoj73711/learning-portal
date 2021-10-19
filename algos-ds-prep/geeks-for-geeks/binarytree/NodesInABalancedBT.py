# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
    
        lh = 0
        ln = root
        while ln is not None:
            lh += 1
            ln = ln.left

        rh = 0
        rn = root
        while rn is not None:
            rh += 1
            rn = rn.right

        if lh == rh:
            return pow(2, lh) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

