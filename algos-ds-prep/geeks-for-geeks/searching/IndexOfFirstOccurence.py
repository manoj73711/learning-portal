class IndexOfFirstOccurenceInSortedArray:

    def binarySearchIterativeBookSol(arr, val):

        low, high = 0, len(arr) - 1
        while low <= high:
            mid = low + high // 2;

            if arr[mid] > val:
                high = mid - 1
            elif arr[mid] < val:
                low = mid + 1
            else:
                if mid == 0 or arr[mid-1]!=arr[mid]:
                    return mid
                else:
                    high = mid -1
        return -1

    def firstOccurenceIndex(self, arr, val):

        idx = self.binarySearchIterative(arr, val)
        if idx == -1:
            return idx

        while idx> 0:
            if arr[idx-1] == arr[idx]:
                idx -=1
        return idx

    def binarySearchIterative(arr, val):

        low, high = 0, len(arr) - 1
        while low <= high:
            mid = low + high // 2;

            if arr[mid] == val:
                return mid
            elif arr[mid] < val:
                low = mid + 1
            else:
                high = mid - 1

        return -1
