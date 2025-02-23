from collections import deque


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        q = deque()
        q.append(1)

        t = 1
        while t <= n:
            t = t * 3
            q.append(t)

        while q and n > 0:
            a = q.pop()
            if a <= n:
                n = n - a

        return True if n == 0 else False


s = Solution()
print(s.checkPowersOfThree(12))
print(s.checkPowersOfThree(91))
print(s.checkPowersOfThree(21))
