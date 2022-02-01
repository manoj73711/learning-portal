class IndexOfLastInSortedArray:

    def indexOfLastOccurenceInArray(self, arr, val):


        low, high = 0, len(arr) - 1
        while low <= high:
            mid = low + high // 2;

            if arr[mid] > val:
                high = mid - 1
            elif arr[mid] < val:
                low = mid + 1
            else:
                if mid == 0 or arr[mid+1]!=arr[mid]:
                    return mid
                else:
                    low = mid +1
        return -1
