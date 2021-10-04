# User function Template for python3
class Solution:

    def minJumps(self, arr, size):

        # This is recursion solution
        def minJumpsRec(a, n):
            if n <= 1:
                return 0
            minJumpCount = float('inf')
            for i in range(n - 1):
                if i + a[i] >= n - 1:
                    sub_result = minJumpsRec(arr, i + 1)
                    if sub_result != float('inf'):
                        minJumpCount = min(minJumpCount, sub_result + 1)
            return minJumpCount

        # TC: o(n^2) SC: o(n)
        def minJumpsDp(a, n):

            dp = [float('inf') for i in range(n)]
            dp[0] = 0

            for i in range(1, n):

                for j in range(0, i):

                    if j + a[j] >= i:
                        if dp[j] != float('inf'):
                            dp[i] = min(dp[i], dp[j] + 1)

            return dp[n - 1]

        return minJumpsDp(arr, size)


