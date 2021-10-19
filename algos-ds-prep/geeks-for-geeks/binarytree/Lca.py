class Solution:
    # Function to return the lowest common ancestor in a Binary Tree.

    def lca(self, root, n1, n2):

        if root is None:
            return None

        if root.data == n1 or root.data == n2:
            return root

        lst = self.lca(root.left, n1, n2)
        rst = self.lca(root.right, n1, n2)

        if lst and rst:
            return root

        if lst:
            return lst
        else:
            return rst

