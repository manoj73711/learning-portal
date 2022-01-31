def allKindsOfNodeDepths(root):
    return allKindsOfNodeDepthsHelper(root).sumOfAllDepths


def allKindsOfNodeDepthsHelper(node):
    if node is None:
        return TreeInfo(0, 0, 0)

    leftTreeInfo = allKindsOfNodeDepthsHelper(node.left)
    rightTreeInfo = allKindsOfNodeDepthsHelper(node.right)

    sumOfLeftTree = leftTreeInfo.sumOfDepths + leftTreeInfo.noOfNodes
    sumOfRightTree = rightTreeInfo.sumOfDepths + rightTreeInfo.noOfNodes

    numNodesInTree = 1 + leftTreeInfo.noOfNodes + rightTreeInfo.noOfNodes

    sumOfDepths = sumOfLeftTree + sumOfRightTree
    sumOfAllDepths = sumOfDepths + leftTreeInfo.sumOfAllDepths + rightTreeInfo.sumOfAllDepths

    return TreeInfo(numNodesInTree, sumOfDepths, sumOfAllDepths)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class TreeInfo:
    def __init__(self, noOfNodes, sumOfDepths, sumOfAllDepths):
        self.noOfNodes = noOfNodes
        self.sumOfDepths = sumOfDepths
        self.sumOfAllDepths = sumOfAllDepths