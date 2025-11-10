from typing import List


class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        stack = []
        res = []
        for x in cost:
            while stack and stack[-1] > x:
                stack.pop()
            if stack:
                res.append(stack[0])
            else:
                res.append(x)
            stack.append(x)
        return res


s = Solution()
print(s.minCosts(cost=[5, 3, 4, 1, 3, 2]))
print(s.minCosts(cost=[1, 2, 4, 6, 7]))
