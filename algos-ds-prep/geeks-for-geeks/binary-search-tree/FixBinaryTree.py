# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        result = [None, None, None]

        self.recoverTreeUtil(root, result)

        if result[0] and result[1]:
            result[0].val, result[1].val = result[1].val, result[0].val
        # first, second, prev

    def recoverTreeUtil(self, root, result):

        if root is None:
            return
        self.recoverTreeUtil(root.left, result)

        if result[2] and root.val < result[2].val:
            if not result[0]:
                result[0] = result[2]
            result[1] = root
        result[2] = root
        self.recoverTreeUtil(root.right, result)

