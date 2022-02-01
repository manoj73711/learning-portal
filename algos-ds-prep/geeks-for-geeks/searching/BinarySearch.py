class BinarySearch:

#this is using iterative solution
    def searchRecursive(self, arr, val):
        return self.searchRecursiveUtil(arr, 0, len(arr)-1, val)

    def searchRecursiveUtil(self, arr, low, high, val):

        if high<low:
            return -1

        mid = low + high // 2
        if arr[mid] == val:
            return mid
        elif arr[mid] < val:
            return self.searchRecursiveUtil(arr, mid+1, high, val)
        else:
            return self.searchRecursiveUtil(arr, low, mid-1, val)




#This is using recursive solution
    
    def binarySearchIterative(arr, val):

        low,high = 0, len(arr)-1
        while low <= high:
            mid = low +high //2;

            if arr[mid] == val:
                return mid
            elif arr[mid] < val:
                low = mid +1
            else:
                high = mid-1

        return -1
