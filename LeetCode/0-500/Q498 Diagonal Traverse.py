from collections import defaultdict
from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        mp = defaultdict(list)
        for r in range(m):
            for c in range(n):
                mp[r + c].append(mat[r][c])
        res = []
        flip = True
        for key in mp.keys():
            if flip:
                res += reversed(mp[key])
            else:
                res += mp[key]
            flip = not flip
        return res


s = Solution()
print(s.findDiagonalOrder(mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # [1,2,4,7,5,3,6,8,9]
print(s.findDiagonalOrder(mat=[[1, 2], [3, 4]]))
