from typing import List


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        l = 0
        for r in range(n):
            if r - l + 1 == 3:
                if nums[l] + nums[r] == nums[l + 1] / 2:
                    res += 1
                l += 1
        return res


s = Solution()
print(s.countSubarrays([1, 2, 1, 4, 1]))
print(s.countSubarrays([1, 1, 1]))
print(s.countSubarrays([2, -7, -6]))
