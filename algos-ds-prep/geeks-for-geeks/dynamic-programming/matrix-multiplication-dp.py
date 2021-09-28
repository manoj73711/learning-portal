class Solution:
    def matrixMultiplication(self, N, arr):

        dp = [[float('inf') for i in range(N)] for i in range(N)]

        for i in range(N - 1):
            dp[i][i + 1] = 0

        for gap in range(2, N):

            for i in range(N):
                if not i + gap < N:
                    break
                j = i + gap

                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + arr[i] * arr[k] * arr[j])

        return dp[0][N - 1]
