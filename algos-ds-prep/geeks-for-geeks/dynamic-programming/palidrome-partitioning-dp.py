class Solution:
    def palindromicPartition(self, string):
        return ppHelper(string, len(string))
        # code here


def isPalindrome(x):
    return x == x[::-1]


def ppHelper(string, n):
    dp = [[float('inf') for i in range(n)] for i in range(n)]

    for i in range(n):
        dp[i][i] = 0

    for gap in range(1, n):

        for i in range(n):
            if i + gap >= n:
                continue
            j = i + gap
            if isPalindrome(string[i::j + 1]):
                dp[i][j] = 0
            else:
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], 1 + dp[i][k] + dp[k + 1][j])
    return dp[0][n - 1]



