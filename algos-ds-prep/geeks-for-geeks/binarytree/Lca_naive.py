# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def findPath(self, root, path, n):

        if root is None:
            return False
        path.append(root.val)

        if root.val == n:
            return True

        if self.findPath(root.left, path, n) or self.findPath(root.right, path, n):
            return True

        path.pop()

        return False

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        path1 = []
        path2 = []

        if self.findPath(root, path1, p) is False or self.findPath(root, path2, q) is False:
            return None

        for i in range(min(len(path1), len(path2)) - 1):
            if path1[i + 1] != path2[i + 1]:
                return path1[i]

        return None


