from collections import defaultdict
from typing import List


class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        mp = defaultdict(int)
        for value, weight in items1:
            mp[value] += weight
        for value, weight in items2:
            mp[value] += weight
        res = []
        for value in sorted(mp.keys()):
            res.append([value, mp[value]])
        return res


s = Solution()
print(s.mergeSimilarItems(items1=[[1, 1], [4, 5], [3, 8]], items2=[[3, 1], [1, 5]]))
print(s.mergeSimilarItems(items1=[[1, 1], [3, 2], [2, 3]], items2=[[2, 1], [3, 2], [1, 3]]))
print(s.mergeSimilarItems(items1=[[1, 3], [2, 2]], items2=[[7, 1], [2, 2], [1, 4]]))
