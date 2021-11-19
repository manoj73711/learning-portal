class Solution:

    def countAndMerge(self, arr, l, m, r):

        n1, n2 = m - l + 1, r - m
        left, right = [0] * n1, [0] * n2

        for i in range(n1):
            left[i] = arr[l + i]
        for j in range(n2):
            right[i] = arr[m + j + 1]

        res,i, j, k = 0, 0, 0, l
        while i < n1 and j < n2:
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                res +=n1-i
                j += 1
            k += 1
        while i < n1:
            arr[k] = left[i]
            i += 1
            k += 1
        while j < n2:
            arr[k] = right[j]
            j += 1
            k += 1
        return res

    def countInv(self, arr, l, r):

        res = 0
        if r > l:
            m = (l + (r - l)) / 2
            res +=self.mergeSort(arr, l, m)
            res +=self.mergeSort(arr, m + 1, r)
            res +=self.merge(arr, l, m, r)
        return res
