class SearchInInfiniteArrays:

    def searchInInfiniteArrays(self, arr, val):

        if arr[0] == val:
            return 0

        i = 1
        while arr[i] < val:
            i = i*2
        if arr[i] == val:
            return i

        return self.binarySearchIterative(arr, val, i/2+1, i)

    def binarySearchIterative(arr, val, low, high):

        while low <= high:
            mid = low + high // 2;

            if arr[mid] == val:
                return mid
            elif arr[mid] < val:
                low = mid + 1
            else:
                high = mid - 1

        return -1
