from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        cur = nums[0]
        for i in range(1, n):
            if cur < nums[i]:
                cur = nums[i]
            else:
                cur += 1
                res += cur - nums[i]
        return res


s = Solution()
print(s.minOperations(nums=[1, 1, 1]))
print(s.minOperations(nums=[1, 5, 2, 4, 1]))
print(s.minOperations(nums=[8]))
