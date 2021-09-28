class subset_sum_problem_naive:
    def isSubsetSum(self, N, arr, sum):
        if N == 0:
            return 1 if sum == 0 else 0

        return self.isSubsetSum(N - 1, arr, sum) + self.isSubsetSum(N - 1, arr, sum - arr[N - 1])
    # code here