from collections import Counter
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)
        res = 0
        for key in freq.keys():
            if key < k:
                res += freq[key]
        return res


s = Solution()
print(s.minOperations(nums=[2, 11, 10, 1, 3], k=10))
print(s.minOperations(nums=[1, 1, 2, 4, 9], k=1))
print(s.minOperations(nums=[1, 1, 2, 4, 9], k=9))
