from collections import defaultdict
from typing import List


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = defaultdict(int)
        res = 0
        l = 0
        for r in range(n):
            freq[nums[r]] += 1
            while freq[nums[r]] > k and l < r:
                freq[nums[l]] -= 1
                if freq[nums[l]] == 0:
                    del freq[nums[l]]
                l += 1
            res = max(res, r - l + 1)
        return res


s = Solution()
print(s.maxSubarrayLength(nums=[1, 2, 3, 1, 2, 3, 1, 2], k=2))
print(s.maxSubarrayLength(nums=[1, 2, 1, 2, 1, 2, 1, 2], k=1))
print(s.maxSubarrayLength(nums=[5, 5, 5, 5, 5, 5, 5], k=4))
