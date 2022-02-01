class TwoPointerApproach:

    def twoPointerApproach(self, arr, n, targetSum):

        first, last = 0, len(arr)-1

        while first < last:
            sum = arr[first]+arr[last]
            if sum == targetSum:
                return True
            elif sum < targetSum:
                first +=1
            else:
                last -=1
        return False

