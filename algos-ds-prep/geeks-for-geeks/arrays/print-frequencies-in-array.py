class solution:

    #TC: O(n) since the array is sorted, if not tc becomes 0(nlogn)
    def printFrequenciesInArray(self, arr, n):

        freq = 1
        i = 1
        while i < n:
            while arr[i] == arr[i-1]:
                freq +=1
                i +=1
            print("Freq of "+arr[i-1]+"is"+freq)
            i += 1
            freq = 1


