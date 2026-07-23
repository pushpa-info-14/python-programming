import bisect
from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        l = bisect.bisect_left(nums, target)
        r = bisect.bisect_right(nums, target)
        return [i for i in range(l, r)]


s = Solution()
print(s.targetIndices(nums=[1, 2, 5, 2, 3], target=2))
print(s.targetIndices(nums=[1, 2, 5, 2, 3], target=3))
print(s.targetIndices(nums=[1, 2, 5, 2, 3], target=5))
