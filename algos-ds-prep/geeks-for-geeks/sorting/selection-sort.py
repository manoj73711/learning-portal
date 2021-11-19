class Solution:

    def selectionSort(self, arr, n):

        for i in range(n - 1):
            min_elem = i
            for j in range(i + 1, n):

                if arr[j] < arr[min_elem]:
                    min_elem = j
            arr[min_elem], arr[i] = arr[i], arr[min_elem]

        return arr

