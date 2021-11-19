class solution:

    #TC: Theta(1)
    def largestElement(self, arr, n):
        res = 0
        for i in range(n):
            if arr[i] > arr[res]:
                res = i
        return res

