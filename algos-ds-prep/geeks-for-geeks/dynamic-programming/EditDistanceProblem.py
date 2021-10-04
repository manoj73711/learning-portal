class Solution:

    def editDistance(self, s, t):

        def editDistanceRec(s, t, m, n):

            if m == 0:
                return n
            if n == 0:
                return m

            if s[m - 1] == t[n - 1]:
                return editDistance(s, t, m - 1, n - 1)
            else:

                return 1 + min(editDistance(s, t, m - 1, n - 1),
                               editDistance(s, t, m - 1, n),
                               editDistance(s, t, m, n - 1))

        def editDistanceDp(s, t, m, n):

            dp = [[float('inf') for i in range(n + 1)] for i in range(m + 1)]

            # Prefil array
            for i in range(n + 1):
                dp[0][i] = i
            for i in range(m + 1):
                dp[i][0] = i

            for i in range(1, m + 1):
                for j in range(1, n + 1):

                    if s[i - 1] == t[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1]
                    else:
                        dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j])
            return dp[m][n]

        return editDistanceDp(s, t, len(s), len(t))
