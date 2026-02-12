from typing import List

from sortedcontainers import SortedList


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        minimum = SortedList()
        maximum = SortedList()
        res = 0
        l = 0
        for r in range(n):
            minimum.add(nums[r])
            maximum.add(nums[r])
            while (maximum[-1] - minimum[0]) * (r - l + 1) > k:
                minimum.remove(nums[l])
                maximum.remove(nums[l])
                l += 1
            res += r - l + 1
        return res


s = Solution()
print(s.countSubarrays(nums=[1, 3, 2], k=4))
print(s.countSubarrays(nums=[5, 5, 5, 5], k=0))
print(s.countSubarrays(nums=[1, 2, 3], k=0))
