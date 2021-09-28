class Solution:
    def isSubsetSum(self, N, arr, sum):

        dp = [[0 for i in range(N + 1)] for i in range(N + 1)]

        for i in range(N + 1):
            dp[i][0] = 1

        for i in range(N + 1):
            for j in range(sum + 1):

                if j - arr[N - 1] < 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1] + dp[i - 1][j - arr[N - 1]]

        return dp[N][sum]
