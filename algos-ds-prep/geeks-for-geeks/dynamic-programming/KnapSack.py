class Solution:

    # Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self, W, wt, val, n):

        # TC = 2^n
        def knapSackRecu(W, wt, val, n):
            if n == 0 or W == 0:
                return 0
            if wt[n - 1] > W:
                return knapSackRecu(W, wt, val, n - 1)
            else:
                return max(knapSackRecu(W, wt, val, n - 1), val[n - 1] + knapSackRecu(W - wt[n - 1], wt, val, n - 1))

        return knapSackRecu(W, wt, val, n)
        # code here
        # Function to return max value that can be put in knapsack of capacity W.
        def knapSack(self, W, wt, val, n):

            def knapSackDpSol(W, wt, val, n):

                dp = [[0 for i in range(W + 1)] for i in range(n + 1)]

                for i in range(1, n + 1):

                    for j in range(1, W + 1):

                        if wt[i - 1] > j:
                            dp[i][j] = dp[i - 1][j]
                        else:
                            dp[i][j] = max(val[i - 1] + dp[i - 1][j - wt[i - 1]], dp[i - 1][j])
                return dp[n][W]
