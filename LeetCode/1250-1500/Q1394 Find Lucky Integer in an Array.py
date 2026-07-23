from collections import Counter
from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = Counter(arr)
        res = -1
        for key in freq.keys():
            if freq[key] == key:
                res = max(res, key)
        return res


s = Solution()
print(s.findLucky(arr=[2, 2, 3, 4]))
print(s.findLucky(arr=[1, 2, 2, 3, 3, 3]))
print(s.findLucky(arr=[2, 2, 2, 3, 3]))
