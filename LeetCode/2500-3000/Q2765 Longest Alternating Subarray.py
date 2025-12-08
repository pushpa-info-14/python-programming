from typing import List


class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        res = -1
        cur = 1
        sign = 1
        i = 1
        while i < n:
            if nums[i] - nums[i - 1] == sign:
                cur += 1
                sign = -sign
            else:
                if cur > 1:
                    res = max(res, cur)
                    i -= 1
                cur = 1
                sign = 1
            i += 1
        if cur > 1:
            res = max(res, cur)
        return res


s = Solution()
print(s.alternatingSubarray(nums=[2, 3, 4, 3, 4]))
print(s.alternatingSubarray(nums=[4, 5, 6]))
print(s.alternatingSubarray(nums=[21, 9, 5]))
