class Solution:
    def minimumFlips(self, n: int) -> int:
        b1 = bin(n)[2:]
        b2 = b1[::-1]
        res = 0
        for i in range(len(b1)):
            if b1[i] != b2[i]:
                res += 1
        return res


s = Solution()
print(s.minimumFlips(7))
print(s.minimumFlips(10))
