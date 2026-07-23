from typing import List


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        res = 0
        prev = 0
        for num in target:
            if num > prev:
                res += (num - prev)
            prev = num
        return res


s = Solution()
print(s.minNumberOperations(target=[1, 2, 3, 2, 1]))
print(s.minNumberOperations(target=[3, 1, 1, 2]))
print(s.minNumberOperations(target=[3, 1, 5, 4, 2]))
