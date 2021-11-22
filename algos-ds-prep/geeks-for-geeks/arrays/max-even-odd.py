class solution:

    #TC: o(n)
    def maxEvenOddSubArray(self, arr, n):
        res = 1
        cur = 1

        for i in range(1, n):

            if (arr[i]%2 ==0 and arr[i-1]%2 != 0) or (arr[i]%2 !=0 and arr[i-1]%2 == 0):
                cur +=1
                res = max(res, cur)
            else:
                cur = 1
        return res

