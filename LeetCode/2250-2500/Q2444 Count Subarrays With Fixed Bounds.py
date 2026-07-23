from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        min_index = -1
        max_index = -1
        invalid_index = -1
        res = 0
        for r in range(n):
            if nums[r] < minK or nums[r] > maxK:
                invalid_index = r
            if nums[r] == minK:
                min_index = r
            if nums[r] == maxK:
                max_index = r
            res += max(min(min_index, max_index) - invalid_index, 0)

        return res


s = Solution()
print(s.countSubarrays(nums=[1, 3, 5, 2, 7, 5], minK=1, maxK=5))
print(s.countSubarrays(nums=[1, 1, 1, 1], minK=1, maxK=1))
