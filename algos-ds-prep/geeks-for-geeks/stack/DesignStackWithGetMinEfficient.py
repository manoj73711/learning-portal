#class solution:

#This used big o(1) aux space for the given problem with some trick

#Given when all the numbers are positive

class NewStack:

    def __init__(self):
        self.stack = []
        self.min = min

    def push(self, val):

        if not self.stack:
            self.min = val
            self.stack.append(val)
        elif val< self.min:
            self.stack.append(x-self.min)
            self.min = val
        else:
            self.stack.append(val)

    def pop(self):
        top = self.stack.pop()
        if top <=0:
            result = self.min
            self.min = self.min-top
            return result
        else:
            return top

    def getMin(self):
        return self.min