from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        seen = set()
        res = -1
        for num in nums:
            if -num in seen:
                res = max(res, abs(num))
            seen.add(num)
        return res


s = Solution()
print(s.findMaxK(nums=[-1, 2, -3, 3]))
print(s.findMaxK(nums=[-1, 10, 6, 7, -7, 1]))
print(s.findMaxK(nums=[-10, 8, 6, 7, -2, -3]))
