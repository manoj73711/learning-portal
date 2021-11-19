class solution:

    def previousGreaterElement(self,a):
        n = len(a)
        result = []
        stck = []
        stck.append(a[0])
        for i in range(n):

            while stck and stck[-1] < a[i]:
                stck.pop()
            if stck:
                result.append(a[i])
            else:
                result.append(-1)
            stck.append(a[i])

        return result



