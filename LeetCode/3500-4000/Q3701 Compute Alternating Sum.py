from typing import List


class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            if i & 1:
                res -= nums[i]
            else:
                res += nums[i]
        return res


s = Solution()
print(s.alternatingSum(nums=[1, 3, 5, 7]))
print(s.alternatingSum(nums=[100]))
