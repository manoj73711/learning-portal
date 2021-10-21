# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, nodeValue, nodeCount):
        self.nodeValue = nodeValue
        self.nodeCount = nodeCount


class Solution:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        treeInfo = TreeInfo(0, 0)
        self.kthSmallestUtil(root, k, treeInfo)
        return treeInfo.nodeValue

    def kthSmallestUtil(self, root, k, treeInfo):

        if root is None or treeInfo.nodeValue >= k:
            return

        self.kthSmallestUtil(root.left, k, treeInfo)

        if treeInfo.nodeCount < k:
            treeInfo.nodeCount += 1
            treeInfo.nodeValue = root.val

        self.kthSmallestUtil(root.right, k, treeInfo)

