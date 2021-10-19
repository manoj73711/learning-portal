# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        maxWidth = 0
        if root is None:
            return maxWidth
        que = deque()
        que.append((root, 0))
        while len(que) > 0:
            size = len(que)
            maxWidth = max(maxWidth, size)
            _, level_head_index = que[0]
            for i in range(size):
                node, col_index = que.popleft()
                if node.left:
                    que.append((node.left, 2 * col_index + 1))
                if node.right:
                    que.append((node.right, 2 * col_index + 2))

                maxWidth = max(maxWidth, col_index - level_head_index + 1)

        return maxWidth

