from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [nums[0]]
        for i in range(1, n):
            res.append(res[i - 1] + nums[i])
        return res


s = Solution()
print(s.runningSum(nums=[1, 2, 3, 4]))
print(s.runningSum(nums=[1, 1, 1, 1, 1]))
print(s.runningSum(nums=[3, 1, 2, 10, 1]))
