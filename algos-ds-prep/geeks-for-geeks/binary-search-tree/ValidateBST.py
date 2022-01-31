import queue


# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    que = queue.Queue()
    que.put(tree)
    is_valid = True
    while not que.empty():
        current_node = que.get()
        if current_node.left is not None:
            que.put(current_node.left)
            if current_node.value < current_node.left.value:
                is_valid = False
                break
        if current_node.right is not None:
            que.put(current_node.right)
            if current_node.value >= current_node.right.value:
                is_valid = False
                break
    return is_valid