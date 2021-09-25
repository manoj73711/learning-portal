class Solution:

    # Function to find minimum number of pages.
    def find_pages(self, A, N, M):

        if N == 1:
            return A[0]
        if M == 1:
            return self.find_sum(A, 0, N - 1)
        res = float('inf')
        for i in range(1, N):
            res = min(res, max(self.find_pages(A, i, M - 1), self.find_sum(A, i, N - 1)))
        return res

    def find_sum(self, A, i, j):

        pages_sum = 0
        for x in range(i, j + 1):
            pages_sum += A[x]

        return pages_sum

