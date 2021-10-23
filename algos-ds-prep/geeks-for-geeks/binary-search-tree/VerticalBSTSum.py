class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    # Complete the function below
    def verticalSum(self, root):

        Map = {}
        height = 0
        Map[height] = root.data

        self.verticalSumUtil(root, height, Map)

        for _, value in Map.items():
            print(value)
        return Map

    def verticalSumUtil(self, root, hd, Map):

        if root == None:
            return

        self.verticalSumUtil(root.left, hd - 1, Map)

        if hd in Map.keys():
            Map[hd] = Map[hd] + root.data
        else:
            Map[hd] = root.data
        self.verticalSumUtil(root.right, hd + 1, Map)
