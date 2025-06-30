from collections import Counter
from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = Counter(nums)
        res = 0
        for num in freq.keys():
            if freq[num] > 0 and freq[num + 1] > 0:
                res = max(res, freq[num] + freq[num + 1])
        return res


s = Solution()
print(s.findLHS(nums=[1, 3, 2, 2, 5, 2, 3, 7]))
print(s.findLHS(nums=[1, 2, 3, 4]))
print(s.findLHS(nums=[1, 1, 1, 1]))
