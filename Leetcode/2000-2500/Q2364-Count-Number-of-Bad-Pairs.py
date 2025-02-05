from collections import defaultdict
from typing import List


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        good_pairs = 0
        prv = defaultdict(int)

        for i in range(n):
            cur = i - nums[i]
            good_pairs += prv[cur]
            prv[cur] += 1

        total_pairs = n * (n - 1) // 2
        return total_pairs - good_pairs


s = Solution()
print(s.countBadPairs([4, 1, 3, 3]))
print(s.countBadPairs([1, 2, 3, 4, 5]))
