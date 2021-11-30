class solution:

    #TC: o(n+k), SC: o(n+k)
    #This is a stable sort
    #This impl supports for objects also
    #Choosen for smaller sets when stability is required
    #Used as a sub routine in radix sort
    def coutingSort(self, arr, n, k):

        count = [0]*k

        for i in range(n):
            count[arr[i]] +=1

        for i in range(1, k):
            count[i] = count[i-1] + count [i]

        output = [0]*n

        for i in range(n-1, -1, -1):

            output[count[arr[i]] -1 ] = arr[i]
            count[arr[i]] -=1
        for i in range(n):
            arr[i] = output[i]
