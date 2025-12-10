from typing import List


class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        mod = 10 ** 9 + 7
        root = complexity[0]
        if root != min(complexity):
            return 0
        count = complexity.count(root)
        if count > 1:
            return 0
        res = 1
        for i in range(1, len(complexity)):
            res = (res * i) % mod
        return res


s = Solution()
print(s.countPermutations(complexity=[1, 2, 3]))
print(s.countPermutations(complexity=[3, 3, 3, 4, 4, 4]))
