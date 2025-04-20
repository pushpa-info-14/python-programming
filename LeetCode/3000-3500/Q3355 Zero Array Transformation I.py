from typing import List


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)

        for l, r in queries:
            diff[l] += 1
            diff[r + 1] -= 1

        accumulated = 0
        for i, num in enumerate(nums):
            accumulated += diff[i]
            if num > accumulated:
                return False
        return True


s = Solution()
print(s.isZeroArray(nums=[1, 0, 1], queries=[[0, 2]]))
print(s.isZeroArray(nums=[4, 3, 2, 1], queries=[[1, 3], [0, 2]]))
print(s.isZeroArray(nums=[3], queries=[[0, 0], [0, 0]]))
print(s.isZeroArray(nums=[2], queries=[[0, 0], [0, 0], [0, 0]]))
print(s.isZeroArray(nums=[0, 5], queries=[[1, 1]]))
