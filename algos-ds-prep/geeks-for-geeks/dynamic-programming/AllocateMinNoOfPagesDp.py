class Solution:

    # Function to find minimum number of pages.
    def find_pages(self, A, N, M):

        dp = [[0 for i in range(N+1)] for i in range(M+1)]
        sum =0
        for j in range(1, N+1):
            sum += A[j-1]
            dp[1][j] = sum

        for i in range(1, M+1):
            dp[i][1] = a[0]

        for i in range(2, M+1):
            for j in range(2, N+1):

                res = float('inf')
                for p in range (1,j):
                    res = min(res, max(dp[i-1][p]), self.find_sum(A, p, j-1))
                dp[i][j] = res
        return dp[M][N]

    def find_sum(self, A, i, j):

        pages_sum = 0
        for x in range(i, j + 1):
            pages_sum += A[x]

        return pages_sum
