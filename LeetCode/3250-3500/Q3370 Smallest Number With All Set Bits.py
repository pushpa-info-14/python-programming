class Solution:
    def smallestNumber(self, n: int) -> int:
        bits = 0
        while n:
            bits += 1
            n //= 2
        return 2 ** bits - 1


s = Solution()
print(s.smallestNumber(5))
print(s.smallestNumber(10))
print(s.smallestNumber(3))
