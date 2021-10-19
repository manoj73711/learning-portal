# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#Construct binary tree from inorder and preorder traversals
class Solution:
    def __init__(self):
        self.pre_index = 0

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        tree = self.buildtreeUtil(inorder, preorder, 0, len(inorder) - 1)
        # Print tree in postorder traversal
        # self.printTree(tree)
        return tree

    def printTree(self, tree):

        if not tree:
            return
        self.printTree(tree.left)
        self.printTree(tree.right)

        print(tree.val)

    def buildtreeUtil(self, inorder, preorder, inorderStart, inOrderEnd):

        if inorderStart > inOrderEnd:
            return None
        tree = TreeNode(preorder[self.pre_index])
        self.pre_index += 1

        foundIndex = -1
        for i in range(inorderStart, inOrderEnd + 1):

            if inorder[i] == tree.val:
                foundIndex = i
                break

        tree.left = self.buildtreeUtil(inorder, preorder, inorderStart, foundIndex - 1)
        tree.right = self.buildtreeUtil(inorder, preorder, foundIndex + 1, inOrderEnd)

        return tree


