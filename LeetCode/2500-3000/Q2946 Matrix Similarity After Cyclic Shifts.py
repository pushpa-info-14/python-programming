from typing import List


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m = len(mat)
        n = len(mat[0])
        temp = []
        k %= n
        for r in range(m):
            cur = mat[r] + mat[r]
            if r % 2 == 0:
                temp.append(cur[k: k + n])
            else:
                temp.append(cur[n - k: n - k + n])
        return mat == temp

    def areSimilar2(self, mat: List[List[int]], k: int) -> bool:
        m = len(mat)
        n = len(mat[0])
        k %= n
        for r in range(m):
            for c in range(n):
                if r % 2 == 0:
                    if mat[r][c] != mat[r][(c + k) % n]:
                        return False
                else:
                    if mat[r][c] != mat[r][(c - k) % n]:
                        return False
        return True


s = Solution()
print(s.areSimilar(mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], k=4))
print(s.areSimilar(mat=[[1, 2, 1, 2], [5, 5, 5, 5], [6, 3, 6, 3]], k=2))
print(s.areSimilar(mat=[[2, 2], [2, 2]], k=3))
print("------------")
print(s.areSimilar2(mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], k=4))
print(s.areSimilar2(mat=[[1, 2, 1, 2], [5, 5, 5, 5], [6, 3, 6, 3]], k=2))
print(s.areSimilar2(mat=[[2, 2], [2, 2]], k=3))
