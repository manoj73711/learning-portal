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

    #This solution is nlogn
    def longestSubsequenceOptimized(self, a, n):

        tail = [0*n]
        len = 1
        tail[0] = a[0]

        for i in range(1, n):

            if a[i] > tail[len-1]:
                tail[len] = a[i]
                len +=1
            else:
                c = self.ceilIdx(a, 0, len-1, a[i])
                tail[c] = a[i]
        return len

    def ceilIdx(self, a, l, r, key):

        while l < r:
            m = (l + (l-r))/2
            if a[m] >= key:
                r = m
            else:
                l = m+1
        return r


