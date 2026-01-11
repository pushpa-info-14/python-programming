from collections import defaultdict
from typing import List


class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        freq = defaultdict(int)
        freq[0] = 1
        res = 0
        prefix_count = 0

        for num in nums:
            if num % modulo == k:
                prefix_count += 1
            prefix_count %= modulo  # To maintain value between 0 - modulo - 1
            rem = (prefix_count - k + modulo) % modulo
            if rem in freq:
                res += freq[rem]
            freq[prefix_count] += 1

        return res


s = Solution()
print(s.countInterestingSubarrays(nums=[3, 2, 4], modulo=2, k=1))
print(s.countInterestingSubarrays(nums=[3, 1, 9, 6], modulo=3, k=0))
