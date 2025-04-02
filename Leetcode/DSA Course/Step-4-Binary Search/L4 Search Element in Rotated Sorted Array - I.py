from typing import List


def search(nums: List[int], target: int):
    n = len(nums)

    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        if nums[low] <= nums[mid]:
            if nums[low] <= target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] <= target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1


print(search([7, 8, 9, 1, 2, 3, 4, 5, 6], 1))
print(search([7, 8, 9, 1, 2, 3, 4, 5, 6], 10))
