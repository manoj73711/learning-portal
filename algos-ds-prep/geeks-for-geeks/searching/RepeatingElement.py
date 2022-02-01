class RepeatingElement:

    #Given max(arr) < n
    def repeatingElement(self, arr, n):

        slow = arr[0]
        fast = arr[arr[0]]
        while slow!=fast:
            slow = arr[slow]
            fast = arr[arr[fast]]
        slow = arr[0]

        while slow!=fast:
            slow = arr[slow]
            fast = arr[arr[fast]]

        return slow

