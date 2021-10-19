#This below code is not found in gfg or leetcode to run and test this program

class Distance:
    def __init__(self):
        self.dist = -1

class Solution:

    def __init__(self):
        self.maxDistance = -1

    def burnBinaryTree(self, tree, leaf):
        dis = Distance()
        self.burnBinaryTreeUtil(tree,Distance(),leaf)
        return dis.dist

    def burnBinaryTreeUtil(self, tree,dist,leaf):

        if tree is None:
            return 0
        if tree.data == leaf:
            dist.dist = 0
            return 1
        ldist = Distance()
        rdist = Distance()

        lh = self.burnBinaryTreeUtil(tree.left,ldist,leaf)
        rh = self.burnBinaryTreeUtil(tree.right, rdist, leaf)

        if ldist.dist!=-1:
            dist.dist = 1 + ldist
            self.maxDistance = max(self.maxDistance, dist.dist + rh)

        elif rdist.dist!=-1:
            dist.dist = 1+rdist
            self.maxDistance = max(self.maxDistance, dist.dist+lh)

        return 1+max(lh,rh)





