class solution:

    #TC: o(n), sc: o(1)
    def maxDifferenceSolution(self, arr):

        res = arr[1] - arr[0]
        minElement = arr[0]

        for j in range(1, n):
            res = max(res, arr[j]-minElement)
            minElement = min(minElement, arr[j])
        return res