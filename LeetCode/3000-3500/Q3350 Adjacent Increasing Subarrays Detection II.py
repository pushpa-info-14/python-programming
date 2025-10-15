from typing import List


class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        prev = 0
        cur = 1
        n = len(nums)
        res = 0
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                cur += 1
            else:
                prev = cur
                cur = 1
            res = max(res, cur // 2)
            res = max(res, min(prev, cur))
        return res


s = Solution()
print(s.maxIncreasingSubarrays(nums=[2, 5, 7, 8, 9, 2, 3, 4, 3, 1]))
print(s.maxIncreasingSubarrays(nums=[1, 2, 3, 4, 4, 4, 4, 5, 6, 7]))
