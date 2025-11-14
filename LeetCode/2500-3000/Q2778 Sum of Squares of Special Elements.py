from typing import List


class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            if n % (i + 1) == 0:
                res += nums[i] * nums[i]
        return res


s = Solution()
print(s.sumOfSquares(nums=[1, 2, 3, 4]))
print(s.sumOfSquares(nums=[2, 7, 1, 19, 18, 3]))
