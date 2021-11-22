class solution:

    def leftRotateAnArrayByOne(self, arr, n):

        if n ==0:
            return arr
        temp = arr[0]
        for i in range(1, n):
            arr[i], arr[i-1] = arr[i-1], arr[i]
        arr[n-1] = temp