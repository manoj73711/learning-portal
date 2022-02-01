class FindPeakElement:

    def findAPeakElement(self, arr, n):

        low, high = 0, n-1

        while low<=high:
            mid = low + high//2

            if (mid == 0 or arr[mid-1] <= arr[mid]) and (mid == n-1 or arr[mid+1] <= arr[mid]):
                return mid
            else:
                if mid>0 and arr[mid-1] > arr[mid]:
                    high = mid-1
                else:
                    low = mid + 1
        return -1