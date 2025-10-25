from typing import List


class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        mini = min(nums)
        maxi = max(nums)
        res = maxi - mini - 2 * k
        return 0 if res < 0 else res


s = Solution()
print(s.smallestRangeI(nums=[1], k=0))
print(s.smallestRangeI(nums=[0, 10], k=2))
print(s.smallestRangeI(nums=[1, 3, 6], k=3))
