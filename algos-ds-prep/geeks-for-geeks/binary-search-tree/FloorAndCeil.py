class Solution:

    #not tested
    def floorOfBst(self, root, key):

        arr = [float('inf')]
        self.floorOfBstUtil(root, key, arr)
        return arr[0]

    #Not tested
    def floorOfBstUtil(self, root, key, arr):

        if not root:
            return root

        if key < root.data:
            self.floorOfBst(root.left)
        elif key > root.data:
            arr[0] = min(arr[0], root.data)
            self.floorOfBst(root.right)
        else:
            arr[0] = root.data

    def floorOfBstRecursiveSolution(self,node, key):

        floor_result = float('inf')
        while node:
            if node.val < key:
                floor_result = min(floor_result, node.val)
                node = node.right

            elif node.val > key:
                node = node.left
            else:
                floor_result = node.val
                return floor_result
        return floor_result

   def ceilOfBstRecursiveSolution(self,node, key):

        ceil_result = 0
        while node:
            if node.val < key:
                node = node.right

            elif node.val > key:
                ceil_result = max(ceil_result, node.val)
                node = node.left
            else:
                floor_result = node.val
                return floor_result
        return ceil_result
