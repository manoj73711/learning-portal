def triplet_with_smaller_sum(arr, target):
    arr.sort()
    triplets = []
    for i in range(len(arr) - 2):
        search_for_smaller_sum(arr, target - arr[i], i, triplets)
    return len(triplets)


def search_for_smaller_sum(arr, target, first, triplets):
    left = first + 1
    right = len(arr) - 1

    while left < right:

        if arr[left] + arr[right] < target:
            for i in range(right, left, -1):
                if arr[left] + arr[i] < target:
                    triplets.append([arr[first], arr[left], arr[i]])
            left += 1
        else:
            right -= 1