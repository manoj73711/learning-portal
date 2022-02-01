class SquareRootFunction:

    #TC: log n
    def squareRootFunction(self, x):

        low, high = 1, x
        res = -1
        while low <= high:
            mid = low + high // 2
            midSq = mid * mid
            if midSq == x:
                return mid
            elif midSq < x:
                low = mid + 1
                res = midSq
            else:
                high = mid - 1
        return res


