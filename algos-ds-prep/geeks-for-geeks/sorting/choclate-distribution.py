class solution:

    def choclateDistribution(self, arr, n, m):

        if m ==0 or n ==0:
            return 0
        arr.sort()
        if m > n:
            return -1
        res = arr[m-1] - arr[0]
        for i in range(1, len(arr)-m+1):
            res = min(res, arr[i+m-1]-arr[i])
        return res



