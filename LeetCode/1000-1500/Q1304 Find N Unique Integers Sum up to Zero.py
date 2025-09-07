from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = [0] if n % 2 != 0 else []
        for i in range(1, n//2 + 1):
            res.append(-i)
            res.append(i)
        return res


s = Solution()
print(s.sumZero(5))
print(s.sumZero(3))
print(s.sumZero(1))
print(s.sumZero(6))
