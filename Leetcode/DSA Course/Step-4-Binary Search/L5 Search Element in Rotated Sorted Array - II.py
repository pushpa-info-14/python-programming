from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)

        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return True
            if nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1
            elif nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return False

s = Solution()
print(s.search([7, 8, 9, 1, 2, 3, 3, 3, 4, 5, 6], 3))
print(s.search([7, 8, 9, 1, 2, 3, 4, 5, 6, 6, 7], 10))
print(s.search([3, 1, 2, 3, 3, 3], 1))
print(s.search([2, 5, 6, 0, 0, 1, 2], 0))
print(s.search([2, 5, 6, 0, 0, 1, 2], 3))
