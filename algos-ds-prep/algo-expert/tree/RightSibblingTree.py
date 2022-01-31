# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def rightSiblingTree(root):
    # Write your code here.
    rightSiblingTreeHelper(root, None, None)

    return root


def rightSiblingTreeHelper(node, nodeParent, isLeftChild):
    if node is None:
        return

    left, right = node.left, node.right

    rightSiblingTreeHelper(left, node, True)

    if nodeParent is None:
        node.right = None
    elif isLeftChild:
        node.right = nodeParent.right
    else:
        if nodeParent.right is None:
            node.right = None
        else:
            node.right = nodeParent.right.left
    rightSiblingTreeHelper(right, node, False)
    return