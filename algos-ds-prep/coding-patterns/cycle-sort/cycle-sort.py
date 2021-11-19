class cycleSort:

    def cyclic_sort(nums):
        i = 0
        while i < len(nums):
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]  # swap
            else:
                i += 1
        return nums