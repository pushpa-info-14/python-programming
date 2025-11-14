from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        for i in range(0, n, 2):
            res += nums[i]
        return res


s = Solution()
print(s.arrayPairSum(nums=[1, 4, 3, 2]))
print(s.arrayPairSum(nums=[6, 2, 6, 5, 1, 2]))
