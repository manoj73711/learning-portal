# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        hashset = set()
        return self.findTargetUtil(root, k, hashset)

    def findTargetUtil(self, root: Optional[TreeNode], k: int, hashtable) -> bool:

        if root is None:
            return False

        if k - root.val in hashtable:
            return True
        hashtable.add(root.val)
        return self.findTargetUtil(root.left, k, hashtable) or self.findTargetUtil(root.right, k, hashtable)

