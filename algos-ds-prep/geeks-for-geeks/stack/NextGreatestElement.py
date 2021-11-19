#Medium problem
class solution:

    def nextGreaterElement(self,a):
        n = len(a)
        result = []
        stck = []
        stck.append(a[n-1])
        for i in range(n-2, -1, -1):

            while stck and stck[-1] < a[i]:
                stck.pop()
            if stck:
                result.append(a[i])
            else:
                result.append(-1)
            stck.append(a[i])
        return result



