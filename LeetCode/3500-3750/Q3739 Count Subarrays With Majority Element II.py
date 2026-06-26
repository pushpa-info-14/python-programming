from typing import List

from sortedcontainers import SortedList


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        p = res = 0
        sl = SortedList([p])
        for x in nums:
            p += 1 if x == target else -1
            res += sl.bisect_left(p)
            sl.add(p)
        return res


s = Solution()
print(s.countMajoritySubarrays(nums=[1, 2, 2, 3], target=2))
print(s.countMajoritySubarrays(nums=[1, 1, 1, 1], target=1))
print(s.countMajoritySubarrays(nums=[1, 2, 3], target=4))
