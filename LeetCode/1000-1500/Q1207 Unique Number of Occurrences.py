from collections import Counter
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        return len(counter.keys()) == len(set(counter.values()))


s = Solution()
print(s.uniqueOccurrences(arr=[1, 2, 2, 1, 1, 3]))
print(s.uniqueOccurrences(arr=[1, 2]))
print(s.uniqueOccurrences(arr=[-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))
