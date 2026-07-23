from typing import List


class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        res = 0
        cur = 0
        for num in nums:
            cur += num
            if cur == 0:
                res += 1
        return res


s = Solution()
print(s.returnToBoundaryCount(nums=[2, 3, -5]))
print(s.returnToBoundaryCount(nums=[3, 2, -3, -4]))
