class Solution:

    # Function to find the maximum number of cuts.
    # tc: 3^n
    def maximizeTheCutsRec(self, n, x, y, z):

        if n == 0:
            return 0
        if n < 0:
            return -1

        res = max(self.maximizeTheCuts(n - x, x, y, z),
                  self.maximizeTheCuts(n - y, x, y, z),
                  self.maximizeTheCuts(n - z, x, y, z))
        if res == -1:
            return res
        return res + 1

    def maximizeTheCuts(self, n, x, y, z):

        dp = [-1 for i in range(n + 1)]
        dp[0] = 0

        for i in range(1, n + 1):

            if i - x >= 0:
                dp[i] = max(dp[i], dp[i - x])
            if i - y >= 0:
                dp[i] = max(dp[i], dp[i - y])
            if i - z >= 0:
                dp[i] = max(dp[i], dp[i - z])

            if dp[i] != -1:
                dp[i] += 1
        return dp[n]
