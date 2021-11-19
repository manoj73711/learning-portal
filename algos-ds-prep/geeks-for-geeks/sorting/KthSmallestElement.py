class solution:

    #nlogn
    #This is the simple and best most preferred algorithm to find kth smallest element
    #This Algorithm name is called quick select algorithm
    def kthSmallestElement(self, arr, k):

        l = 0
        r = len(arr) -1

        while l <=r:

            p = self.lumitoPartition(arr,l,r)

            if p == k-1:
                return p
            elif p > k-1:
                r = p-1
            else:
                l = p+1
        return -1


    def lumitoPartition(self, arr, l, h):

        #Consider the last element as greater element always
        pivot = arr[h]
        i = -l
        for j in range(l, h):
            if arr[j] < pivot:
                i +=1
                #do swapping
                arr[j], arr[i] = arr[i], arr[j]
        arr[i+1], arr[h] = arr[h], arr[i+1]
        return i+1

