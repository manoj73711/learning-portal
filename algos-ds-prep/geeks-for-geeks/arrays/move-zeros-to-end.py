class solution:

    def moveZerosToEnd(self, arr, n):

        count =0
        for i in range(n):
            if arr[i]!=0:
                arr[i], arr[count] = arr[count], arr[i]
                count +=1
                