class Solution:
    # Function to return the total number of possible unique BST.
    def numTrees(self, N):

        dp = [0 for i in range(N + 1)]

        dp[0] = 1

        for i in range(1, N + 1):
            for k in range(i):
                dp[i] += dp[k] * dp[i - k - 1]

        return dp[N]
        # code here
