import math


class Solution:
    def internalAngles(self, sides: list[int]) -> list[float]:
        sides.sort()
        a, b, c = sides
        if (a + b) <= c:
            return []
        a1 = math.degrees(math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)))
        b1 = math.degrees(math.acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c)))
        c1 = math.degrees(math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b)))

        res = [a1, b1, c1]
        res.sort()
        return res


s = Solution()
print(s.internalAngles(sides=[3, 4, 5]))
print(s.internalAngles(sides=[2, 4, 2]))
