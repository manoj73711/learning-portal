
class solution:

    def quickSort(self, arr, l, h):

        if l<h:
            p = self.partition(arr,l,h)
            self.quickSort(arr,l, p)
            self.quickSort(arr, p+1, h)
    #hoares algorithm
    def partition(self, arr, l, h):

        pivot = arr[l]
        i = l-1
        j = h+1

        while True:
            i +=1
            while arr[i]<pivot:
                i +=1
            j -=1
            while arr[j]<pivot:
                j -=1
            if i >= j:
                return j
            arr[i], arr[j] = arr[j], arr[i]


