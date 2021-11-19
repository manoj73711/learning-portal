class solution:

    #tc: O(NLOGN)
    def minDifferenceInArray(self, arr, n):
        arr.sort()
        res = float("inf")
        for i in range(1, n):
            res = min (res, arr[i]-arr[i-1])
        return res

