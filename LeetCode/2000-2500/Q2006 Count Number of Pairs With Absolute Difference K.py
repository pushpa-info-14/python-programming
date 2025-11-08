from collections import Counter
from typing import List


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)
        nums = sorted(list(freq.keys()))
        res = 0
        for x in nums:
            if x + k in freq:
                res += freq[x] * freq[x + k]
        return res


s = Solution()
print(s.countKDifference(nums=[1, 2, 2, 1], k=1))
print(s.countKDifference(nums=[1, 3], k=3))
print(s.countKDifference(nums=[3, 2, 1, 5, 4], k=2))
