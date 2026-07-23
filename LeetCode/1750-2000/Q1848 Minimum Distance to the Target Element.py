from typing import List


class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        n = len(nums)
        d = n
        for i in range(n):
            if nums[i] == target:
                cur = abs(i - start)
                if d > cur:
                    d = cur
        return d


s = Solution()
print(s.getMinDistance(nums=[1, 2, 3, 4, 5], target=5, start=3))
print(s.getMinDistance(nums=[1], target=1, start=0))
print(s.getMinDistance(nums=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], target=1, start=0))
