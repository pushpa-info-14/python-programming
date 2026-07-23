from collections import Counter, defaultdict
from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        freq = Counter(nums)
        range_freq = defaultdict(int)
        for num in nums:
            range_freq[num - k] += 1
            range_freq[num] -= 1
            range_freq[num + 1] += 1
            range_freq[num + k + 1] -= 1
        cur = 0
        res = 0
        for k in sorted(range_freq.keys()):
            cur += range_freq[k]
            res = max(res, freq[k] + min(numOperations, cur))
        return res


s = Solution()
print(s.maxFrequency(nums=[1, 4, 5], k=1, numOperations=2))  # 2
print(s.maxFrequency(nums=[5, 11, 20, 20], k=5, numOperations=1))  # 2
print(s.maxFrequency(nums=[5, 11, 20, 20, 20, 20], k=5, numOperations=1))
print(s.maxFrequency(nums=[5, 11, 20, 20, 20, 20], k=5, numOperations=4))
print(s.maxFrequency(nums=[88, 53], k=27, numOperations=2))  # 2
print(s.maxFrequency(nums=[1, 90], k=76, numOperations=1))  # 1
print(s.maxFrequency(nums=[23, 54], k=77, numOperations=1))  # 2
print(s.maxFrequency(nums=[37, 30, 37], k=26, numOperations=1))  # 3
