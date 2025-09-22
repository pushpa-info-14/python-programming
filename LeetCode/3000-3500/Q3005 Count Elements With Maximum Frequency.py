from collections import Counter
from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)
        max_freq = max(freq.values())
        res = 0
        for count in freq.values():
            if count == max_freq:
                res += max_freq
        return res


s = Solution()
print(s.maxFrequencyElements(nums=[1, 2, 2, 3, 1, 4]))
print(s.maxFrequencyElements(nums=[1, 2, 3, 4, 5]))
