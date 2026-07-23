from collections import Counter
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        counter = Counter(arr1)
        for x in arr2:
            res += [x] * counter[x]
            del counter[x]
        for x in sorted(counter.keys()):
            res += [x] * counter[x]
        return res


s = Solution()
print(s.relativeSortArray(arr1=[2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], arr2=[2, 1, 4, 3, 9, 6]))
print(s.relativeSortArray(arr1=[28, 6, 22, 8, 44, 17], arr2=[22, 28, 8, 6]))
