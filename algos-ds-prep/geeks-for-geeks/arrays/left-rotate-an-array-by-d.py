class solution:

    def leftRotateAnArrayByOne(self, arr, n):

        if n == 0:
            return arr
        temp = arr[0]
        for i in range(1, n):
            arr[i], arr[i-1] = arr[i-1], arr[i]
        arr[n-1] = temp

    #TC: o(n), sc: o(d)
    def leftRotateAnArrayByDPlacesMethod2(self, arr, n, d):

        temp = []

        for i in range(d):
            temp.append(arr[i])

        for i in range(d, n):
            arr[i-d] = arr[i]

        for i in range(d):
            arr[n-d+i] = temp[i]

        return arr

    #TC: o(n), sc: o(1)
    def leftRotateAnArrayByDPlacesMethod3(self, arr, n, d):

        self.reverseArray(arr, 0, d-1)
        self.reverseArray(arr, d, n-1)
        self.reverseArray(arr, 0, n-1)

        return arr

    def reverseArray(self, arr, i, j):

        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i +=1
            j -=1

