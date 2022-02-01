class SortedRotatedArray:

    def sortedRotatedArray(self, arr, val):

        low, high = 0, len(arr)-1
        while low <= high:

            mid = low + high // 2

            if arr[mid] == val:
                return mid

            #Left half sorted
            elif arr[low] < arr[mid]:

                if val >= arr[low] < val and val < arr[mid]:
                    high = mid-1
                else:
                    low = mid+1
            else:
                #Right half sorted
                if val > arr[mid] and val <= arr[high]:
                    low = mid+1
                else:
                    high = mid-1

        return -1