class Solution:
    def hammingDistance(self, x: int, y: int) -> int:

        res = 0
        while x > 0 or y > 0:
            if x & 1 != y & 1:
                res += 1
            x = x >> 1
            y = y >> 1
        return res


s = Solution()
print(s.hammingDistance(1, 4))
print(s.hammingDistance(3, 1))
