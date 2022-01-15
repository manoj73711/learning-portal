# Function to find the maximum possible amount of money we can win.
class Solution:
    def optimalStrategyOfGame(self, arr, n):
        def optimalRecur(arr, i, j):
            if i + 1 == j:
                return max(arr[i], arr[j])
            return max(arr[i] + min(optimalRecur(arr, i + 2, j), optimalRecur(arr, i + 1, j - 1)),
                       arr[j] + min(optimalRecur(arr, i + 1, j - 1), optimalRecur(arr, i, j - 2)))

        return optimalRecur(arr, 0, len(arr) - 1)
        # code here

    def optimalDp(arr, n):

        dp = [[0 for i in range(n)] for i in range(n)]

        for i in range(n - 1):
            dp[i][i + 1] = max(arr[i], arr[i + 1])

        for gap in range(3, n):

            for i in range(n):
                j = i + gap
                if j >= n:
                    break
                dp[i][j] = max(arr[i] + min(dp[i + 2][j], dp[i + 1][j - 1]),
                               arr[j] + min(dp[i + 1][j - 1], dp[i][j - 2]))
            gap = gap + 1
        return dp[0][n - 1]
