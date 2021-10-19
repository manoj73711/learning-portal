# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#Working solution
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = list(list())
        if root is None:
            return root
        que = deque()
        stack = []
        reverse = False
        que.append(root)
        while len(que) > 0:
            n = len(que)
            lis = []
            for i in range(n):
                node = que.popleft()

                if reverse:
                    stack.append(node.val)
                else:
                    lis.append(node.val)
                    # print(node.data, end = "")

                if node.left is not None:
                    que.append(node.left)
                if node.right is not None:
                    que.append(node.right)
            if reverse:
                while len(stack) > 0:
                    # print(stack.pop(), end = "")
                    lis.append(stack.pop())

            reverse = not reverse
            if len(lis) > 0:
                result.append(lis)

        return result

#This is alternate solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = list(list())
        if root is None:
            return root
        s1 = []
        s2 = []
        s1.append(root)
        while len(s1) > 0 or len(s2) > 0:
            lis = list()

            while len(s1) > 0:
                n1 = s1.pop()
                lis.append(n1.val)
                if n1.left is not None:
                    s2.append(n1.left)
                if n1.right is not None:
                    s2.append(n1.right)

            if len(lis) > 0:
                result.append(list)
                lis.clear()

            while len(s2) > 0:
                node = s2.pop()
                lis.append(node.val)
                if node.left is not None:
                    s1.append(node.left)
                if node.right is not None:
                    s1.append(node.right)
            if len(lis) > 0:
                result.append(lis)
        return result
