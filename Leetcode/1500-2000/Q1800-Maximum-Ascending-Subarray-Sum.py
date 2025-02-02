from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]

        res = nums[0]
        curr = nums[0]
        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                curr += nums[i]
                res = max(res, curr)
            else:
                curr = nums[i]
        return res


s = Solution()
print(s.maxAscendingSum([10, 20, 30, 5, 10, 50]))
print(s.maxAscendingSum([10, 20, 30, 40, 50]))
print(s.maxAscendingSum([12, 17, 15, 13, 10, 11, 12]))
print(s.maxAscendingSum([100, 10, 1]))
print(s.maxAscendingSum([3,6,10,1,8,9,9,8,9]))
