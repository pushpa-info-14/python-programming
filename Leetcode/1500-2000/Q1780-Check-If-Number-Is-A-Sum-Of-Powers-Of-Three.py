from collections import deque


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        q = deque()
        q.append(1)

        power = 1
        while power <= n:
            power *= 3
            q.append(power)

        while q and n > 0:
            power = q.pop()
            if power <= n:
                n -= power

        return True if n == 0 else False

    def checkPowersOfThree2(self, n: int) -> bool:
        while n:
            if n % 3 == 2:
                return False
            n //= 3

        return True


s = Solution()
print(s.checkPowersOfThree(12))
print(s.checkPowersOfThree(91))
print(s.checkPowersOfThree(21))
print(s.checkPowersOfThree2(12))
print(s.checkPowersOfThree2(91))
print(s.checkPowersOfThree2(21))
