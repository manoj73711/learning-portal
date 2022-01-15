class Solution:
    # Method 1
    # Function to return the level order traversal of a tree.
    def levelOrder(self, root):

        if root is None:
            return

        que = []
        que.append(root)
        que.append(None)

        while len(que) > 0:

            print(que[0].data)
            node = que.pop()

            # Thi
            # s is to print level by level in new line
            if node is None:
                print( / n)
                que.append(None)
                continue

            if node.left is not None:
                que.append(node.left)

            if node.right is not None:
                que.append(node.right)

    # This is secondary solution for level order traversal, This is more efficient
    def levelOrderMethod2(self, root):

        if root is None:
            return

        que = []
        que.append(root)

        while len(que) > 0:

            node = que.pop()
            size = len(que)

            for i in range(size):
                node = que.pop()
                print(node.data)

                if node.left is not None:
                    que.append(node.left)

                if node.right is not None:
                    que.append(node.right)
            print(\n)
