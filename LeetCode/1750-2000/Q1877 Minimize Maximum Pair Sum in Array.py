from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        i = 0
        j = n - 1
        while i < j:
            res = max(res, nums[i] + nums[j])
            i += 1
            j -= 1
        return res


s = Solution()
print(s.minPairSum(nums=[3, 5, 2, 3]))
print(s.minPairSum(nums=[3, 5, 4, 2, 4, 6]))
