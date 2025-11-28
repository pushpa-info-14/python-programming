from collections import Counter
from typing import List


class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        pairs = 0
        leftovers = 0
        for key, value in counter.items():
            pairs += value // 2
            leftovers += value % 2
        return [pairs, leftovers]


s = Solution()
print(s.numberOfPairs(nums=[1, 3, 2, 1, 3, 2, 2]))
print(s.numberOfPairs(nums=[1, 1]))
print(s.numberOfPairs(nums=[0]))
