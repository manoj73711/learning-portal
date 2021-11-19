class TwoStacks:

    def __init__(self, n):
        self.size = n
        self.array = [None] * n
        self.top1 = -1
        self.top2 = n

    def push1(self,a, x):

        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.array[self.top1] = x
        else:
            print('stack 1 is full')

    def push2(self,a, x):

        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.array[self.top2] = x
        else:
            print('stack 1 is full')

    def pop1(self, a):

        if self.top1 > 0:
            elem = self.array[self.top1]
            self.top1 -= 1
            return elem
        else:
            print('stack 1 is empty')
            return None

    # code here

    # Function to remove an element from top of the stack2.
    def pop2(self,a):
        if self.top2 < self.size - 1:
            elem = self.array[self.top2]
            self.top2 += 1
            return elem
        else:
            print('stack 2 is empty')
            return None
# code here

