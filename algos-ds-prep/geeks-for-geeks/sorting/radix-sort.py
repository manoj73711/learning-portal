class solution:

    # O(N), SC: 0(N)
    #This is stable and objects can be sorted too
    #This is preferred to eliminate the 0(n+k) because when k is n^2 tc becomes n^2
    def radixSort(self, arr, n):

        maxElem = arr[0]
        for i in range(1, n):
            maxElem = max(maxElem, arr[i])

        exp = 1
        while maxElem/exp > 0:
            self.radixCountingSort(arr, exp)
            exp = exp*10

    def radixCountingSort(self, arr, n, exp):

        count = [0]*10
        for i in range(n):
            count[(arr[i]/exp)%10] +=1
        for i in range(1,10):
            count[i] = count[i-1] + count[i]

        output = [0]*n

        for i in range(n-1, -1, -1):
            output[count[(arr[i]/10) % 10] -1 ] = arr[i]
            count[arr[i]] -=1
        for i in range(n):
            arr[i] = output[i]
