from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        n = len(nums)
        res = []
        for i in range(n):
            res.insert(index[i], nums[i])
        return res


s = Solution()
print(s.createTargetArray(nums=[0, 1, 2, 3, 4], index=[0, 1, 2, 2, 1]))
print(s.createTargetArray(nums=[1, 2, 3, 4, 0], index=[0, 1, 2, 3, 0]))
print(s.createTargetArray(nums=[1], index=[0]))
print(s.createTargetArray(nums=[4, 2, 4, 3, 2], index=[0, 0, 1, 3, 1]))  # [2,2,4,4,3]
