from typing import List


class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:

        def f(n):
            curr = 1
            total = 0
            while curr <= n:
                total += n - curr + 1
                curr <<= 2
            return total

        return sum((f(r) - f(l - 1) + 1) // 2 for l, r in queries)

s = Solution()
print(s.minOperations(queries = [[1,2],[2,4]]))
print(s.minOperations(queries = [[2,6]]))