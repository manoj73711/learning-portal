class solution:

    #Many duplicate elements are present from 1 to n in the array and find the duplicates
    def find_missing_numbers(nums):
        i = 0
        while i < len(nums):
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]  # swap
            else:
                i += 1

        missingNumbers = []

        for i in range(len(nums)):
            if nums[i] != i + 1:
                missingNumbers.append(i + 1)

        return missingNumbers

    #Find the repeating number of same kind and return that only one number
    def find_duplicate(a):

        i, n = 0, len(a)

        while i < n:
            if a[i] != i + 1:
                j = a[i] - 1
                if a[i] != a[j]:
                    a[i], a[j] = a[j], a[i]
                else:
                    return a[i]
            else:
                i += 1

        # TODO: Write your code here
        return -1

