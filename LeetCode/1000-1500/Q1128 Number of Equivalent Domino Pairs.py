from collections import defaultdict
from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        freq = defaultdict(int)
        res = 0
        for x, y in dominoes:
            if x < y:
                freq[(x, y)] += 1
            else:
                freq[(y, x)] += 1

        for i in freq.values():
            res += (i * (i - 1) // 2)

        return res


s = Solution()
print(s.numEquivDominoPairs(dominoes=[[1, 2], [2, 1], [3, 4], [5, 6]]))
print(s.numEquivDominoPairs(dominoes=[[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]))
print(s.numEquivDominoPairs(dominoes=[[2, 2], [1, 2], [1, 2], [1, 1], [1, 2], [1, 1], [2, 2]]))
print(s.numEquivDominoPairs(dominoes=[[2, 1], [1, 2], [1, 2], [1, 2], [2, 1], [1, 1], [1, 2], [2, 2]]))  # 15
