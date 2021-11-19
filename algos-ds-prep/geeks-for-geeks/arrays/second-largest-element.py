class solution:

    #TC 0(n)
    def secondLargestElement(self, arr, n):

        result = -1
        largest = 0

        for i in range(n):

            if arr[i] > arr[largest]:
                result = largest
                largest = i
            elif result == -1 or arr[i] > arr[result]:
                result = i
        return result