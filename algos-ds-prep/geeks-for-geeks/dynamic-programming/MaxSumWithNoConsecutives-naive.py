class Solution:
    # max_sum_with_no_consecutives
    def max_sum_no_consec(self,arr,N):

        if N ==1:
            return arr[0]
        elif N == 2:
            return max(arr[0], arr[1])

        return max(self.max_sum_no_consec(self, arr, N-1), self.max_sum_no_consec(self, arr, N-1)+arr[N-1])