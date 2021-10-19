class Solution:

      def getSize(node):

        if node is None:
            return 0
        return 1+getSize(node.left)+getSize(node.right)
        # code here
