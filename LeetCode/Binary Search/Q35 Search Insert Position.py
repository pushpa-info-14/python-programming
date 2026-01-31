from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[-1] < target:
            return len(nums)
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l


s = Solution()
print(s.searchInsert([1, 3, 5, 6], 5))  # 2
print(s.searchInsert([1, 3, 5, 6], 2))  # 1
print(s.searchInsert([1, 3, 5, 6], 7))  # 4
