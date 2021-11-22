class solution:

    #TC: o(n)
    def checkArrayIsSorted(self, arr, n):

        for i in range(1, n):
            if arr[i] < arr[i-1]:
                return False
        return True