class solution:

    #TC: o(n), sc: o(1)
    def maxConsecutive1s(self, arr, n):
        res = 0
        cur = 0
        for i in range(n):
            if arr[i] == 1:
                cur +=1
                res = max(res, cur)
            else:
                cur = 0

        return res