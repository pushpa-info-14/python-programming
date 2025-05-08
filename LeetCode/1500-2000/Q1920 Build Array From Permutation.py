from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        for i in range(n):
            res[i] = nums[nums[i]]

        return res


s = Solution()
print(s.buildArray(nums=[0, 2, 1, 5, 3, 4]))
print(s.buildArray(nums=[5, 0, 1, 2, 3, 4]))
