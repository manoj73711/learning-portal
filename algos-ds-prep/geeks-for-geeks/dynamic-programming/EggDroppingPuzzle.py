class Solution:

    # Function to find minimum number of attempts needed in
    # order to find the critical floor.
    # n - eggs, k - floors
    def eggDrop(self, n, k):

        dp = [[float('inf') for i in range(n + 1)] for i in range(k + 1)]

        # prefil as per base conditions
        for i in range(1, n + 1):
            dp[0][i] = 0
            dp[1][i] = 1

        for i in range(k + 1):
            dp[i][1] = i

        for i in range(2, k + 1):

            for j in range(2, n + 1):

                for x in range(1, i + 1):
                    dp[i][j] = min(dp[i][j], 1 + max(dp[x - 1][j - 1], dp[i - x][j]))

        return dp[k][n]
