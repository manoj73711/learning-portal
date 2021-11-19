#class solution:


class NewStack:

    def __init__(self):
        self.stack = []
        self.aux_stack = []

    def push(self, val):

        self.stack.append(val)
        if val < self.aux_stack[-1]:
            self.aux_stack.append(val)

    def pop(self):

        val = self.stack.pop()
        if self.aux_stack[-1] == val:
            self.aux_stack.pop()
        return val

    def getMin(self):
        return self.aux_stack[-1]