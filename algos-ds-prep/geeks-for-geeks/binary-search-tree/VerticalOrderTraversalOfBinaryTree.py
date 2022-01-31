
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#TC: o(nlogn) SC: o(d)
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        result_list = list(list())
        que = deque()
        que.append((root, 0))

        result_map = {}

        while len(que) > 0:

            node, hd = que.popleft()
            if hd in result_map.keys():
                result_map[hd].append(node.val)
            else:
                result_map[hd] = [node.val]

            if node.left:
                que.append((node.left, hd - 1))
            if node.right:
                que.append((node.right, hd + 1))

        # sort the map

        for value in sorted(result_map.keys()):
            result_list.append(sorted(result_map[value]))

        return result_list



