class Solution:

    # Function to find length of longest increasing subsequence.
    def longestSubsequence(self, a, n):

        dp = [1 for i in range(n)]

        for i in range(1, n):

            max_val = 1
            for j in range(i):
                if a[j] < a[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        max_element = dp[0]
        for i in range(n):
            max_element = max(max_element, dp[i])

        return max_element
        # code here
