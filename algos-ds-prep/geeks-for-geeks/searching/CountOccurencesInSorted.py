#TC: o(logn)
class CountOccurencesInSorted:

    def countOccurencesInSorted(self, arr, val):

        first = self.indexOfFirstOccurenceInArray(arr, val)

        if first == -1:
            return 0
        return self.indexOfLastOccurenceInArray(arr, val)-first +1


    def indexOfFirstOccurenceInArray(arr, val):

        low, high = 0, len(arr) - 1
        while low <= high:
            mid = low + high // 2;

            if arr[mid] > val:
                high = mid - 1
            elif arr[mid] < val:
                low = mid + 1
            else:
                if mid == 0 or arr[mid - 1] != arr[mid]:
                    return mid
                else:
                    high = mid - 1
        return -1

    def indexOfLastOccurenceInArray(self, arr, val):

        low, high = 0, len(arr) - 1
        while low <= high:
            mid = low + high // 2;

            if arr[mid] > val:
                high = mid - 1
            elif arr[mid] < val:
                low = mid + 1
            else:
                if mid == 0 or arr[mid + 1] != arr[mid]:
                    return mid
                else:
                    low = mid + 1
        return -1

