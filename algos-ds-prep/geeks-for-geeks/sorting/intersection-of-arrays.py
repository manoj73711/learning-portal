class Solution:

    def NumberofElementsInIntersection(self, a, b, n, m):

        count = 0
        i, j = 0, 0
        while i < n and j < m:

            if i > 0 and a[i] == a[i - 1]:
                i += 1
                continue
            if a[i] < b[j]:
                i += 1
            elif a[i] > b[j]:
                j += 1
            else:
                count += 1
                i += 1
                j += 1
        return count
        # return: expected length of the intersection array.