from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # The center must appear in all the edges
        a, b = edges[0]
        c, d = edges[1]
        if a in [c, d]:
            return a
        else:
            return b


s = Solution()
print(s.findCenter(edges=[[1, 2], [2, 3], [4, 2]]))
print(s.findCenter(edges=[[1, 2], [5, 1], [1, 3], [1, 4]]))
