from collections import defaultdict
from typing import List


class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = defaultdict(int)
        max_freq = 0
        l = 0
        for r in range(n):
            freq[nums[r]] += 1
            max_freq = max(max_freq, freq[nums[r]])
            while r - l + 1 - max_freq > k:
                freq[nums[l]] -= 1
                if freq[nums[l]] == 0:
                    del freq[nums[l]]
                l += 1

        return max_freq


s = Solution()
print(s.longestEqualSubarray(nums=[1, 3, 2, 3, 1, 3], k=3))
print(s.longestEqualSubarray(nums=[1, 1, 2, 2, 1, 1], k=2))
print(s.longestEqualSubarray(nums=[1], k=0))
print(s.longestEqualSubarray(nums=[4, 4, 2, 2, 4], k=1))
