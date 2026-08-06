class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for x in range(n, n + 100):
            cur = x
            product = 1
            while cur:
                product *= cur % 10
                cur //= 10
            if product % t == 0:
                return x
        return 0


s = Solution()
print(s.smallestNumber(n=10, t=2))
print(s.smallestNumber(n=15, t=3))
