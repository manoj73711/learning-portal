class solution:

    #TC: o(n)
    def removeDuplicates(self, arr, n):
        result = 1
        for i in range(1, n):
            if arr[i] != arr[result-1]:
                arr[result] = arr[i]
                result += 1
        return result