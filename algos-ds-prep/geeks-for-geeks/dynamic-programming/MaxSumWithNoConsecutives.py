class Solution:
    # max_sum_with_no_consecutives
    def max_sum_no_consec(self,arr,N):

        if N ==1:
            return arr[0]
        elif N ==2:
            return max(arr[0],arr[1])

        dp = [0 for i in range(N+1)]
        dp[1] = arr[0]
        dp[2] = max(arr[0], arr[1])

        for i in range(3,N+1):
            dp[i] = max(arr[i-1]+dp[i-2], dp[i-1])
        return arr[N]
